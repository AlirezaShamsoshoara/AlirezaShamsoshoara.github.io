import assert from 'node:assert/strict';
import { ACTIONS, MAP, DEFAULTS, GUIDED_ACTIONS, tdUpdate, transition, createRandom, createLearner, createGuidedWalkthrough, createExplorationTrace, greedyRollout, formatQ } from '../../assets/js/rl/qlearning-core.mjs';

let passed = 0;
function test(name, check) { check(); passed += 1; console.log(`PASS ${name}`); }
function near(actual, expected) { assert.ok(Math.abs(actual - expected) < 1e-12, `${actual} != ${expected}`); }
const example = params => tdUpdate({ oldValue: 2, reward: 1, nextValues: [1, 2, 4, 1.5], alpha: .5, gamma: .9, ...params });

test('generic one-cell continuing arithmetic remains correct', () => { const r=example();near(r.target,4.6);near(r.error,2.6);near(r.newValue,3.3); });
test('true termination suppresses only the future term', () => { const r=example({terminated:true});near(r.target,1);near(r.newValue,1.5); });
test('alpha and gamma endpoints remain distinct', () => { near(example({alpha:0}).newValue,2);near(example({alpha:1}).newValue,4.6);near(example({gamma:0}).target,1);near(example({gamma:1}).target,5); });
test('zero residual, not zero reward alone, means no correction', () => { const r=tdUpdate({oldValue:.45,reward:0,nextValues:[.5],alpha:.1,gamma:.9});near(r.error,0);near(r.newValue,.45); });
test('input validation rejects nonfinite or invalid settings', () => { for(const p of [{alpha:-1},{gamma:1.1},{reward:NaN},{terminated:1},{nextValues:[]}])assert.throws(()=>example(p)); });
test('the action order and stated map are shared', () => { assert.deepEqual(ACTIONS,['Left','Down','Right','Up']);assert.deepEqual(MAP,['SFFF','FHFH','FFFH','HFFG']);assert.equal(DEFAULTS.alpha,.1);assert.equal(DEFAULTS.gamma,.95); });
test('native safe, wall, hole and goal transitions are correct', () => { assert.equal(transition(0,0).nextState,0);assert.equal(transition(0,1).nextState,4);assert.equal(transition(4,2).hole,true);assert.equal(transition(4,2).reward,0);const g=transition(14,2);assert.equal(g.goal,true);assert.equal(g.reward,1);assert.equal(g.terminated,true);assert.throws(()=>transition(5,2));assert.throws(()=>transition(15,0)); });
test('guided data are 36 real transitions across six goal-reaching episodes', () => { const t=createGuidedWalkthrough();assert.deepEqual(t.states,[0,4,8,9,13,14,15]);assert.equal(t.records.length,36);assert.equal(t.goals,6);for(const r of t.records){assert.equal(r.behavior,'guided');assert.equal(r.state,t.states[r.episodeStep-1]);assert.equal(r.nextState,t.states[r.episodeStep]);assert.equal(r.action,GUIDED_ACTIONS[r.episodeStep-1]);assert.equal(r.terminated,r.episodeStep===6);assert.equal(r.reward,r.episodeStep===6?1:0);assert.equal(r.truncated,false);} });
test('first episode changes nothing until the true-terminal goal', () => { const t=createGuidedWalkthrough();for(const r of t.records.slice(0,5)){near(r.target,0);near(r.error,0);assert.deepEqual(r.qBefore,r.qAfter);}const g=t.records[5];near(g.target,1);near(g.error,1);near(g.newValue,.1);near(g.bootstrap,0);near(g.qAfter[13][2],0);near(g.qAfter[0][1],0); });
test('second episode propagates the old goal estimate on an actual later revisit', () => { const r=createGuidedWalkthrough().records[10];assert.equal(r.episode,2);assert.equal(r.state,13);assert.equal(r.nextState,14);near(r.nextMax,.1);near(r.target,.095);near(r.newValue,.0095);assert.equal(r.terminated,false); });
test('third episode reaches an earlier state, not instant backward rewriting', () => { const r=createGuidedWalkthrough().records[15];assert.equal(r.episode,3);assert.equal(r.state,9);assert.equal(r.action,1);near(r.nextMax,.0095);near(r.target,.009025);near(r.newValue,.0009025); });
test('the sixth episode is the first positive start-state update', () => { const t=createGuidedWalkthrough();for(const r of t.records.slice(0,30))near(r.qAfter[0][1],0);const r=t.records[30];assert.equal(r.episode,6);assert.equal(r.state,0);assert.ok(r.newValue>0);near(r.newValue,7.737809375e-7); });
test('every changed entry is exactly the experienced state/action', () => { for(const r of createGuidedWalkthrough().records){const changed=[];for(let s=0;s<16;s++)for(let a=0;a<4;a++)if(r.qBefore[s][a]!==r.qAfter[s][a])changed.push([s,a]);assert.deepEqual(changed,r.increment===0?[]:[[r.state,r.action]]);} });
test('tables persist between transitions and episodes without hidden interpolation', () => { const t=createGuidedWalkthrough();for(let i=1;i<t.records.length;i++)assert.deepEqual(t.records[i].qBefore,t.records[i-1].qAfter);const l=createLearner();for(let e=0;e<6;e++)for(const a of GUIDED_ACTIONS)l.step(a);assert.deepEqual(l.snapshot().q,t.finalQ); });
test('record tables and the trace cannot be mutated by seeking', () => { const t=createGuidedWalkthrough();assert.throws(()=>{t.records[5].qAfter[14][2]=500;});assert.throws(()=>{t.records.push({});});assert.equal(t.records[5].qAfter[14][2],.1); });
test('terminal hole/goal rows remain zero', () => { const t=createGuidedWalkthrough();for(const s of [5,7,11,12,15])assert.deepEqual(t.finalQ[s],[0,0,0,0]); });
test('forced teaching actions do not consume exploration RNG', () => { const a=createLearner({epsilon:1}),b=createLearner({epsilon:1});for(const action of GUIDED_ACTIONS)a.step(action);assert.equal(a.step().action,b.step().action); });
test('invalid guided actions fail before state or RNG changes', () => { const a=createLearner(),b=createLearner();const before=a.snapshot();assert.throws(()=>a.step(4));assert.deepEqual(a.snapshot(),before);assert.deepEqual(a.step(),b.step()); });
test('an external cap retains a positive next-state bootstrap', () => { const l=createLearner({maxSteps:6});for(const a of GUIDED_ACTIONS)l.step(a);let r;for(const a of [0,1,1,2,1,2])r=l.step(a);assert.equal(r.nextState,14);assert.equal(r.truncated,true);assert.equal(r.terminated,false);near(r.bootstrap,.095);near(r.newValue,.0095); });
test('zero learning rate freezes the trace; zero discount prevents upstream propagation', () => { const a=createGuidedWalkthrough({alpha:0});assert.ok(a.finalQ.flat().every(v=>v===0));const g=createGuidedWalkthrough({gamma:0});near(g.finalQ[13][2],0);assert.ok(g.finalQ[14][2]>0); });
test('tiny positive estimates are never displayed as zero', () => { assert.equal(formatQ(0),'0');assert.equal(formatQ(7.737809375e-7),'7.738e-7');assert.equal(formatQ(.0009025),'9.025e-4');assert.equal(formatQ(.0095),'0.0095');assert.equal(formatQ(.1),'0.1');assert.throws(()=>formatQ(NaN)); });
test('guided settings and episode counts are validated', () => { for(const p of [{episodes:0},{episodes:51},{episodes:1.5},{alpha:NaN},{gamma:-1}])assert.throws(()=>createGuidedWalkthrough(p)); });
test('default exploratory data collection remains reproducible', () => { const a=createLearner(),b=createLearner();a.train(500);b.train(500);assert.deepEqual(a.snapshot(),b.snapshot());assert.equal(a.snapshot().goals,267);assert.equal(a.snapshot().holes,233);assert.equal(a.snapshot().interactions,3336); });
test('frozen greedy replay reaches the goal without learner mutation', () => { const l=createLearner();l.train(500);const before=l.snapshot();const route=greedyRollout(before.q);assert.equal(route.goal,true);assert.equal(route.transitions.length,6);assert.deepEqual(l.snapshot(),before); });
test('untrained first-argmax replay honestly reaches the cap, not a goal', () => { const r=greedyRollout(createLearner().snapshot().q);assert.equal(r.goal,false);assert.equal(r.truncated,true);assert.equal(r.transitions.length,60); });
test('snapshots are owned copies and parameter/index settings remain strict', () => { const l=createLearner();const s=l.snapshot();s.q[0][0]=500;assert.equal(l.snapshot().q[0][0],0);assert.throws(()=>createLearner({epsilon:2}));assert.throws(()=>createLearner({maxSteps:0}));assert.throws(()=>createRandom(-1));assert.throws(()=>l.train(0));assert.throws(()=>greedyRollout([])); });
test('milestone explanations have reading holds shared with media and autoplay', () => {
  const t=createGuidedWalkthrough();
  for(const index of [5,10,30]) {
    const timing=t.records[index].phaseDurationsMs;
    assert.deepEqual(timing,[600,720,2500,2500,2800,3800]);
    assert.throws(()=>{timing[2]=1;});
  }
  assert.ok(t.records[0].phaseDurationsMs[2]<500);
  assert.equal(t.records.flatMap(r=>r.phaseDurationsMs).reduce((a,b)=>a+b,0),112920);
});
test('every episode retains a different goal-adjacent estimate, despite the identical route', () => {
  const t=createGuidedWalkthrough();
  const start=[0,.1,.19,.271,.3439,.40951],end=[.1,.19,.271,.3439,.40951,.468559];
  for(let episode=0;episode<6;episode++) {
    near(t.records[episode*6].qBefore[14][2],start[episode]);
    near(t.records[episode*6+5].qAfter[14][2],end[episode]);
    assert.notDeepEqual(t.records[episode*6].qBefore,t.finalQ);
  }
  assert.equal(new Set(start).size,6);assert.equal(new Set(end).size,6);
});
test('the detailed lesson uses real exploratory actions and varied episode lengths', () => {
  const t=createExplorationTrace();
  assert.equal(t.records.length,843);assert.equal(t.episodeSummaries.length,120);
  assert.deepEqual(t.episodeSummaries.slice(0,3).map(e=>e.length),[12,5,4]);
  assert.notDeepEqual(t.episodeSummaries[0].states,t.episodeSummaries[1].states);
  assert.ok(t.records.every(r=>r.behavior==='epsilon-greedy'&&r.selection!=='guided'));
  assert.ok(t.records.some(r=>r.hole)&&t.records.some(r=>r.goal));
});
test('exploration labels follow the recorded coin flip, not a hand-picked action', () => {
  const t=createExplorationTrace();
  for(const r of t.records) {
    assert.equal(r.selection==='explore',r.exploreDraw<r.epsilon);
    if(r.selection!=='explore') {
      const row=r.qBefore[r.state],maximum=Math.max(...row);
      assert.equal(row[r.action],maximum);
      assert.equal(r.selection==='greedy-tie',row.filter(value=>value===maximum).length>1);
    }
  }
  assert.equal(t.records.filter(r=>r.selection==='explore').length,262);
});
test('epsilon endpoints control the random branch, while maximal ties are separate', () => {
  assert.ok(createExplorationTrace({epsilon:1,episodes:10}).records.every(r=>r.selection==='explore'));
  const zero=createExplorationTrace({epsilon:0,episodes:10});
  assert.ok(zero.records.every(r=>r.selection!=='explore'));
  assert.ok(zero.records.some(r=>r.selection==='greedy-tie'));
});
test('every exploration record is an actual native transition with one-cell learning', () => {
  for(const r of createExplorationTrace().records) {
    const native=transition(r.state,r.action);
    assert.equal(r.nextState,native.nextState);assert.equal(r.reward,native.reward);assert.equal(r.terminated,native.terminated);
    const changed=[];
    for(let s=0;s<16;s++)for(let a=0;a<4;a++)if(r.qBefore[s][a]!==r.qAfter[s][a])changed.push([s,a]);
    assert.deepEqual(changed,r.increment===0?[]:[[r.state,r.action]]);
  }
});
test('exploratory episode resets retain the table and never step from a terminal', () => {
  const t=createExplorationTrace();
  for(let i=1;i<t.records.length;i++)assert.deepEqual(t.records[i].qBefore,t.records[i-1].qAfter);
  for(const e of t.episodeSummaries) {
    assert.equal(e.length,e.endIndex-e.startIndex+1);
    assert.equal(t.records[e.startIndex].state,0);
    assert.ok(t.records[e.endIndex].terminated||t.records[e.endIndex].truncated);
  }
});
test('observed milestones are discovered honestly at their actual episode positions', () => {
  const t=createExplorationTrace();
  assert.deepEqual(t.milestones,{explore:0,hole:11,reward:210,bootstrap:550,start:735});
  assert.equal(t.records[210].episode,29);near(t.records[210].newValue,.1);
  assert.equal(t.records[550].episode,70);near(t.records[550].newValue,.0095);
  assert.equal(t.records[735].episode,103);near(t.records[735].newValue,2.86298946875e-6);
  assert.ok(t.records.slice(0,210).every(r=>r.qAfter.flat().every(value=>value===0)));
});
test('detailed and batched learning match when given the same settings and budget', () => {
  const t=createExplorationTrace(),l=createLearner();l.train(120);
  assert.deepEqual(t.finalQ,l.snapshot().q);assert.equal(t.goals,l.snapshot().goals);assert.equal(t.holes,l.snapshot().holes);
});
test('edited highlights are explicitly a subset of whole recorded episodes', () => {
  const t=createExplorationTrace();
  assert.equal(t.highlightIndices.length,40);
  assert.deepEqual([...new Set(t.highlightIndices.map(i=>t.records[i].episode))],[1,2,29,70,103]);
  assert.ok(t.highlightIndices.length<t.records.length);
  for(const e of t.episodeSummaries.filter(e=>t.highlightIndices.includes(e.startIndex)))
    assert.ok(Array.from({length:e.length},(_,i)=>e.startIndex+i).every(i=>t.highlightIndices.includes(i)));
});
test('exploration tables, paths, and selection records are frozen', () => {
  const t=createExplorationTrace();
  assert.throws(()=>{t.records[210].qAfter[14][2]=50;});
  assert.throws(()=>{t.episodeSummaries[0].states[0]=4;});
  assert.throws(()=>{t.highlightIndices.push(99);});
});
test('unsupported budgets fail and absent early rewards are not fabricated', () => {
  for(const p of [{episodes:0},{episodes:251},{episodes:1.2},{epsilon:2},{seed:-1}])assert.throws(()=>createExplorationTrace(p));
  const short=createExplorationTrace({episodes:20});
  assert.equal(short.milestones.reward,null);assert.equal(short.milestones.bootstrap,null);assert.equal(short.goals,0);
});
const trace=createExplorationTrace();
console.log(JSON.stringify({tests_passed:passed,episodes:trace.episodes,records:trace.records.length,milestones:trace.milestones,
  key_updates:Object.entries(trace.milestones).map(([name,index])=>{const r=trace.records[index];return{name,index,episode:r.episode,state:r.state,action:r.action,nextState:r.nextState,reward:r.reward,target:r.target,newValue:r.newValue};})},null,2));
