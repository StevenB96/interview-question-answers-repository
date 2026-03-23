# Problem Solving & Scenario Based Questions

___

### 1. How do you go about troubleshooting a complex bug?

1. Reproduce the issue – Replicate the bug consistently and record the exact steps, inputs, environment, and timestamps to ensure you are investigating the real problem.
2. Gather evidence – Review logs, stack traces, metrics, error rates, and recent deployments or configuration changes to narrow the scope of the issue.
3. Protect users if necessary – If the bug is impacting users, apply a quick mitigation such as a feature flag, rollback, or temporary safeguard while investigating.
4. Form hypotheses – Identify two or three plausible root causes and design quick tests to confirm or rule them out.
5. Add targeted instrumentation – Use selective logs, metrics, or breakpoints to observe behaviour without introducing risky or widespread code changes.
6. Implement and test the fix – Once the root cause is confirmed, implement the fix and add unit or integration tests to prevent recurrence.
7. Roll out safely – Deploy using a controlled method such as a feature flag or canary release and monitor for regressions before full rollout.
8. Document the outcome – Record the root cause, fix, and lessons learned so the team can avoid similar issues and debug faster in the future.

___

### 2. Explain how you would debug an unfamiliar codebase

1. Build initial context – If possible, speak with the original author and review the README, architecture docs, and run the application locally to understand how it behaves.
2. Identify entry points – Locate main modules, routes, or tests and follow the data flow through the system using code search and git history.
3. Understand the data model – Examine the core data structures or database schema to understand the domain and where key logic is likely implemented.
4. Run small components – Execute tests, scripts, or small runnable units to observe runtime behaviour and see where transformations or errors occur.
5. Validate assumptions with tools – Use debugging tools, targeted logs, or small tests to confirm how the system actually behaves.
6. Document and share insights – Take concise notes and update documentation to accelerate onboarding and confirm your understanding with teammates.

___

### 3. What strategies do you use to debug a complex algorithm? ✔

* Use minimal reproducible inputs – Create small test cases and compare them with known-correct examples to identify where the algorithm’s behaviour diverges.
* Add assertions and invariants – Insert checks at key steps so the code validates its own assumptions and detects errors early.
* Trace intermediate values – Use targeted logging or a debugger to inspect intermediate state and find where the computation starts to deviate.
* Check edge cases and data types – Verify boundary conditions, input types, and numerical stability issues such as rounding errors or overflow.
* Break the algorithm into smaller parts – Refactor complex logic into smaller functions and unit-test each component to simplify reasoning.
* Profile for performance – If performance matters, identify bottlenecks with profiling tools and evaluate more efficient algorithms or data structures.
* Add regression tests – Include tests for boundary conditions and numerical stability to ensure the issue does not reappear in future changes.


___

### 4. How would you evaluate a new feature request to decide whether to implement it? (Should we do this?) ✔

1. Clarify the problem and users – Understand what issue the feature solves, who it helps, and which metrics (e.g., engagement, conversion) it should improve.
2. Check strategic alignment – Ensure the feature supports product goals and fits the roadmap, while identifying dependencies and potential risks.
3. Consider simpler alternatives – Evaluate whether a smaller MVP or experiment could validate the idea before committing to a full implementation.
4. Assess impact vs effort – Estimate the expected value of the feature compared to the development time and long-term maintenance cost.
5. Use prioritisation frameworks – Apply tools like RICE or the Eisenhower matrix to compare this feature objectively against other work.
6. Define success criteria – Set measurable acceptance criteria and monitoring so the team can evaluate whether the feature delivers value after release.
7. Gain stakeholder alignment – Confirm agreement with product, engineering, and other stakeholders, and plan a controlled rollout (e.g., feature flags or staged release).
8. Ship a small validated increment first – Release an initial version to gather real user feedback, reduce risk, and iterate based on actual usage.

___

### 5. How do you decide if a solution is the best approach to a problem? (What is the best way to do it?) *referenced ✔

I start by defining clear evaluation criteria such as flexibility, performance, reliability, security, maintainability, time-to-ship, and cost. I then score each candidate solution against these criteria to highlight the key trade-offs. Making the criteria explicit helps ensure the decision-making process aligns with the team’s goals and constraints.

Next, I prioritise the most important criteria. If there is no clear differentiator, I consider secondary factors such as technical debt, observability and monitoring, and potential on-call or operational load. When uncertainty is high. I consult stakeholders and teammates to ensure alignment. I may build a small prototype or spike to gather data. Prototyping helps reduce guesswork and provides measurable evidence.

Finally, I make the decision transparent by documenting the reasoning and keeping a fallback plan ready. This ensures that if the chosen approach underperforms, the team can pivot quickly with minimal disruption and a clear record of why the decision was made.

___

### 6. Explain how you would optimise an inefficient algorithm. (Profiling, improving complexity). ✔

I’d start by measuring: add benchmarks and profile to confirm the actual slow parts. Measurement prevents premature optimisation and focuses effort on real bottlenecks rather than perceived ones. I prefer micro-benchmarks that isolate the hot path and system-level tests to confirm end-to-end impact.

Then I’d analyse algorithmic complexity to spot hotspots like nested loops, repeated computations or unnecessary recursion. I’d replace inefficient data structures with more appropriate ones (hash maps, heaps, tries), apply memoisation, caching or precomputation where applicable, and reduce work by removing unnecessary copies or extra iterations. Processing elements lazily or streaming can also cut memory and CPU use.

If it’s CPU-bound and safe, I’d consider parallelisation or asynchronous processing, but only after verifying correctness and measuring. Finally I’d re-run benchmarks and add regression/performance tests so improvements are repeatable and don’t regress later. The goal is measurable change: lower latency, lower CPU, or reduced memory usage for the same correctness.

___

### 7. Describe your process for identifying performance bottlenecks. (Profiling tools, metrics). ✔

I start by defining clear performance goals such as p50, p95 and p99 latency, throughput, and resource limits. Explicit goals make trade-offs visible and allow us to prioritise optimisations by user impact rather than micro-optimisations.

I then collect logs, system metrics and traces to see where latency concentrates, using OpenTelemetry to send traces to Jaeger and metrics to Prometheus, which I visualise in Grafana. I use profilers to identify CPU hotspots and memory leaks, and I check database queries with EXPLAIN, network latencies using browser devtools, and third-party service times. Correlating traces with deployments or traffic spikes helps detect regressions.

Finally, I prioritise bottlenecks by impact versus cost, apply targeted optimisations, and re-measure to ensure improvements hold. I also add monitoring and alerts so regressions are caught early — turning discovery into ongoing prevention rather than one-off fixes.

___

### 8. What techniques do you use to test and validate your code? (Unit tests, integration tests). ✔

I follow the test pyramid: many fast unit tests, focused integration tests, and a few end-to-end tests. Fast unit tests provide quick feedback loops for developers while integration and contract tests guard cross-service behaviour. That balance keeps CI fast and confidence high.

I use mocks and stubs for external dependencies and contract tests for APIs, and add edge-case and unexpected-input tests when appropriate. I automate tests in CI along with linting, static analysis, and type checks. In addition, I maintain regression tests for reported bugs and incorporate those into the suite so fixes stay fixed.

I also rely on code review and pair programming for quality and knowledge sharing, and add monitoring and health checks in production so we get early signals if something slips. Together this creates a feedback loop from dev to production that reduces surprises and enables faster, safer releases.

___

### 9. What would you do if a production issue occurred during off-hours? / How would you approach a system outage or critical failure? ✔

I acknowledge the incident promptly and follow the runbook or escalation policy. I perform a preliminary assessment to determine severity and quickly implement the safest mitigation, such as a rollback, feature flag, or failover. The first goal is protecting users and stabilising the system, not perfect fixes.

I keep concise, regular updates to stakeholders and the incident channel, prioritising service restoration before deep diagnosis. I involve the right people early — ops, SRE, or the author of recent changes — and use pairing to speed diagnosis. Once stable, I document the timeline and decisions so the postmortem has accurate context.

After stabilisation, I perform a blameless postmortem, implement fixes, and update runbooks and alerts to prevent similar issues in the future. The continuous loop (mitigate → fix → learn → prevent) reduces MTTR over time and improves system resilience.

___

### 10. If you discovered a security vulnerability in your app, how would you respond? ✔

If I discovered a security vulnerability in an app, I would first contain the issue by disabling the vulnerable surface or applying a temporary mitigation without destroying evidence. Containment preserves forensic data and limits exposure while we plan a safe fix.

I would notify the security team and leadership, following responsible disclosure and compliance procedures. Next, I would perform a preliminary assessment to determine severity, create an action plan for a safe fix, and test it thoroughly in staging. I’d also check for related vulnerabilities and whether the issue could have been exploited.

I would then patch the vulnerability, deploy safely, and monitor for any exploitation attempts. Finally, I would communicate to affected stakeholders per policy and update threat models, tests, and monitoring so the same issue is less likely to recur. The emphasis is on fast containment, transparent communication, and durable prevention.

___

### 11. How do you stay calm and focused when debugging under pressure? ✔

When debugging under pressure, I follow a structured checklist — reproduce the issue, isolate the cause, form hypotheses, and test — which helps reduce random attempts and keeps me focused. The checklist converts pressure into an organised process so progress is visible even if the path is slow.

I prioritise restoring service with minimal risk through quick mitigation before digging into the root cause. I use pairing to gain a fresh perspective and share the cognitive load, and take short breaks if I get stuck to avoid tunnel vision. These tactics keep decision quality high under stress.

Throughout the process, I communicate clearly and frequently so stakeholders’ expectations are managed. That reduces panic, allows us to mobilise the right people, and ensures a smoother transition to post-incident analysis and preventive actions.

___

### 12. How do you approach optimising a slow-loading web page? ✔

I start by measuring real user and lab metrics such as First Contentful Paint, Largest Contentful Paint, Time to Interactive, and total byte weight to identify bottlenecks. Real-user metrics reveal the actual experience across networks and devices, which guides prioritisation.

I then optimise the critical rendering path by deferring or asynchronously loading non-critical JavaScript, inlining critical CSS, and minimising render-blocking resources. I optimise assets through responsive images, modern formats, and compression, and use caching and a CDN for static assets alongside server-side improvements like compression and caching. I also lazy-load below-the-fold content and reduce third-party scripts to improve perceived speed.

Finally, I monitor performance across devices and geographies to validate improvements and guard against regressions. The result is measurable better UX — faster interactive times and improved engagement — rather than subjective optimism about speed.

___

### 13. Describe a time you analysed data before making a decision. (e.g. A/B test results). ✔

Project references: 2PD

For my general prioritisation approach, please see **“How do you decide if a solution is the best approach to a problem? (What is the best way to do it?)”**. 

On a project (codename 2PD), I had to choose the best layout for the clinical charting interface, which shows patient sensor data and treatment progress.

The criteria I used were clear from the start:
- speed — how quickly clinicians could read the key metrics,
- accuracy — how often they interpreted the data correctly,
- usability across devices — especially desktop vs tablet, and
- practical implementation factors — like maintainability and clinical auditability.

We compared two options:

- A: table-based layout — dense rows and columns with raw values, which was precise but harder to scan quickly.
- B: visual chart-based layout — charts and highlights showing trends more clearly, which was designed to make patterns easier to spot.

We ran a small usability test with clinical staff, randomising which version they saw. I measured task completion time, errors or misinterpretations, and satisfaction, then segmented the results by device type to see whether the best option changed in different contexts.

The results showed that B reduced average task time by 22%, reduced errors by 15%, and had better satisfaction scores. Based on that, we chose B for rollout and documented the decision so the reasoning was clear for the team and for clinical review. The data-driven choice improved clinician speed.

___

### 14. Tell me about a project where you had to think creatively to solve a problem. ✔

Project references: 2PD

On a project (codename 2PD), I inherited a Java mobile app that initially only had a GameState class managing local progress and scores, while we were developing the backend from scratch as an MVC system. I was tasked with implementing secure OAuth-style authentication and automatic syncing of game state to the backend.

**To achieve this**, I enhanced the existing GameState class by adding listeners so that any major change — such as step completion — would trigger callbacks automatically. I then introduced a GameService class to observe these changes and handle all network syncing, keeping the UI layer completely decoupled from backend logic. The networking logic was encapsulated in an ApiClient, which not only performed HTTP requests for syncing but also handled user logins, working with an AuthInterceptor to securely attach OAuth tokens, while a SecureStore and AuthManager managed the tokens safely.

This architecture allowed the app to sync game state automatically, securely, and efficiently, while reusing the existing GameState class and maintaining a clean, maintainable structure.