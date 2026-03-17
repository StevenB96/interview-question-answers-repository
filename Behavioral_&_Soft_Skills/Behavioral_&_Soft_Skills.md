# Behavioural & Soft Skills

_Italics = Reflection_
**Bold = Main Point**

___

### 1. Tell me about yourself. (Give a concise personal introduction). ✔

Hi — I’m Steven, a full-stack developer with three years’ consulting experience and a master’s in engineering. I’ve delivered end-to-end web and mobile solutions — from API design and databases to frontend UX and deployment. I communicate across disciplines and enjoy owning work from concept through production.

Recently I took a focused break to upskill in cloud, generative AI and modern frameworks, and I’ve been building hands-on projects to apply those skills. I use those projects to validate patterns and produce shareable artifacts that speed future work for teams.

I’m looking to join a team where I can own features end-to-end and help deliver scalable, user-focused products, including pragmatic AI integrations. My aim is to turn those skills into measurable improvements in reliability, speed-to-market, and user satisfaction.

___

### 2. Why do you want to be a software/full-stack developer? ✔

I became a full-stack developer because software brings together the parts of engineering I enjoy most: problem solving, systems thinking, and especially rapid feedback loops. My multidisciplinary engineering background lets me prototype solutions quickly and measure real impact, so I can translate product needs into practical technical solutions.

I enjoy both implementing clear requirements and using my systems knowledge to suggest improvements. **For example**, I’ve led initiatives that reduced customer queries by 31% and eliminated the need for manual data entry — outcomes that reinforced my belief I can use initiative to deliver measurable business impact.

Beyond technical fundamentals, I’m keen to work across cross-functional teams, which is integral to great software. I find satisfaction in partnering with others to overcome challenges, remove blockers, and ensure solutions align with product, design, and operations to speed delivery and reduce friction.

___


### 3. What are your greatest strengths and weaknesses? ✔

<u>Strengths</u>

Commitment to continuous development — I actively seek feedback and look for ways to improve my skills. I attend conferences and meetups, such as React and Django events, and take targeted courses to keep my knowledge current and practical. That habit helps me introduce useful patterns and reduce ramp time on new tech.

Team integration — I bring positive energy to teams and make a deliberate effort to build strong working relationships. I enjoy mentoring colleagues and organising informal touchpoints, such as virtual lunch sessions, to help maintain team cohesion, even in remote environments. These small investments tend to reduce misunderstandings and speed collaboration.

<u>Weaknesses</u>

Over-analysing problems too early — I sometimes spend too much time researching and exploring options before validating my assumptions with others. This can slow progress and delay decision-making in fast-moving projects. To address this, I now sanity-check my understanding with a colleague early and time-box initial research to around 30–60 minutes. This ensures I gather enough context without over-investing in exploration.

Judging the right level of documentation — While documentation is important for handovers and complex systems, over-documenting can slow delivery and create unnecessary maintenance overhead. To improve, I now focus on documenting intent and key interfaces — for example, core data entities, environment variables, and high-level sequences — while favouring concise diagrams, short READMEs, or inline comments. I also include ownership and review dates so documentation stays accurate and actionable.

___


### 4. Describe your biggest professional achievement to date. ✔

Project references: OFM

My biggest achievement was leading the stage-one delivery of a project (codename OFM), which delivered a mobile app and an admin portal. The work required location services, push notifications, and integrating WordPress as the authoritative source for location and news content.

Technically, I designed a robust data model and implemented a Python ETL and data-normalisation script that synchronises CMS content via its API and runs automatically as a cron job. I drafted a technical options document for complex business logic and led a face-to-face session with the customer and team to agree a pragmatic solution. 

From a teamwork and delivery perspective, I decomposed features into clear work packages, estimated tasks, and coordinated delivery through sprint routines and daily scrums. I mentored two junior engineers through pair programming, daily check-ins and structured code reviews to accelerate their ramp-up and ensure consistent code quality, and I maintained standards through pull requests, paired sessions and acceptance-testing workflows.

We delivered the MVP, the client commissioned follow-on work, and the junior developers became productive contributors. This demonstrated my ability to own technical design, deliver on time, and mentor others to the point where they could ship independently.

___


### 5. What is the hardest problem you’ve solved, and how did you solve it? / Describe a time you faced a significant challenge and how you overcame it? ✔

Project references: obs-etl-k8s-demo-project

For my general debugging approach, please see **"How do you go about troubleshooting a complex bug? (Walk through your process).”**. 

**For example**, on my project obs-etl-k8s-demo-project, an Airflow container refused to start and a downstream service broke. The logs suggested a Redis version mismatch, but changing the Redis environment variable did not resolve the issue. I approached the problem methodically: inspecting logs, testing configuration changes, searching GitHub and Stack Overflow, and using LLM tools to explore additional hypotheses. This helped keep the investigation structured.

The main challenges were that the problem could not easily be reproduced or reduced to a smaller test case, there was no clear breaking change to identify, and none of the investigated solutions resolved the issue or pointed clearly to the root cause, which slowed progress.

Eventually, I audited the container image tags and discovered an upstream image availability/policy issue. I resolved the problem by migrating to the community-maintained image. The experience reinforced the value of systematic debugging, persistent research, and validating key assumptions—such as image availability and validity—early in the process to reduce time-to-recovery.

___

### 6. Tell me about a time you failed or received criticism and what you learned. ✔

Project references: BC

Early in my career, on a project (codename BC), I bundled several form features together to be efficient, which caused scope creep and made the first ticket overrun. Because the client had Kanban access and could see progress, their confidence dropped and they paused the project. I was told I should have consulted stakeholders before deviating from the agreed ticket-by-ticket approach.

I realised I’d treated hard sprint deadlines as the only constraint and hadn’t confirmed I had the freedom to change the planned approach. 

I learned that transparency and alignment are as important as efficiency. Since then I surface proposed deviations early to get stakeholder buy-in, update the backlog with the team before changing course, and ensure stakeholders are informed whenever we change scope or approach. That practice preserves trust and prevents surprises.

___

### 7. How do you handle tight deadlines or stressful situations? ✔ — similar to "How would you handle a situation where priorities change suddenly"?

Project references: BD

I begin with prioritisation of features. For my general prioritisation approach, please see **“How do you prioritise tasks when given multiple priorities?”**. 

With priorities set, I break features into small, testable tasks, timebox work where useful, and keep the team and stakeholders updated so blockers surface early and decisions about scope are clear. That shared visibility makes it straightforward to decide what to cut or defer when time is limited.

On a project (codename BD), the client repeatedly announced features publicly before they were ready, so I focused the team on demo-critical items, ran frequent internal check-ins, and kept the client informed about progress and trade-offs. By concentrating on the essentials and maintaining tight feedback loops, we delivered what mattered for the demo without surprises and preserved our credibility.

This approach helps keep morale steady under pressure and ensures the team delivers the highest-impact work within the deadline.

___

### 8. Give an example of working effectively under pressure. ✔

Project references: ACF

I inherited a “poison-chalice” as the primary developer on a project (codename ACF) where database migrations would not run, meaning I had to reverse-engineer the domain from the codebase while still delivering features. In situations like this, I rely on a consistent process: focused rapid learning, structured investigation and instrumentation, and proactive stakeholder communication.

I quickly learned Node.js and GraphQL, instrumented the application to trace data flows, and produced an entity–relationship diagram (ERD) to clarify the domain structure. I also organised customer sessions to validate assumptions and fill gaps in understanding. By diagnosing and resolving runtime and SQL compatibility issues, I was able to get the system running again, deliver the required features, and produce a domain report so the team could continue development.

These deliverables removed a major blocker and allowed other developers to pick up work with clear documentation and minimal ramp-up. Having a structured plan helped me stay confident I was on track and enabled me to perform effectively under pressure.

___

### 9. Describe a conflict you had with a teammate and how you resolved it. ✔

I inherited a module refactored into a large pure-SQL query, with no tests or notes. The author argued it was faster; I argued it reduced readability and maintainability. We both had valid concerns: performance vs clarity.

After discussion I pointed out that I had to maintain the code, so we agreed I’d revert the main branch for immediate maintainability. Then I wrapped the SQL in a documented, tested function and added a performance test so we kept the speed benefit but regained clarity. We validated the approach with a benchmark to make the trade-offs explicit.

We resolved it with benchmarks, documentation and a pragmatic compromise. The result preserved performance while reducing long-term maintenance risk and improving team confidence in the code.

___

### 10. How do you receive and act on feedback? / How do you handle feedback or criticism from peers/managers?

Project references: ai_tool-risk_mitigation-demo-project, obs-etl-k8s-demo-project

I always thank people for feedback, then turn it into an action plan I can validate. After interviews I received feedback that I needed more exposure to production debugging. I converted that feedback into a hands-on project.

I built an Observability & ETL demo to practise deployment and monitoring. I set success criteria, sought peer review and iterated until the project demonstrated the skills required.

I set success criteria, sought peer review and iterated — feedback became a measurable improvement loop. That process helped me both learn new skills and produce tangible evidence of impact.

___

### 11. How do you prioritise tasks when given multiple priorities? ✔

I start by estimating impact versus effort, often using frameworks like RICE or the Eisenhower matrix, to identify high-value work. In general, I prioritise tasks that deliver the greatest value for the least effort, but I also allow hard deadlines or operational needs to adjust the order when necessary. The goal is to maximise impact while keeping commitments realistic and achievable.

Next, I apply some pragmatic checks around dependencies and blockers. These can include missing credentials, third-party services, resource constraints, or the availability of subject-matter experts. Identifying these early helps avoid stalled work. Where possible, I also group related tasks together to reduce context switching and maintain momentum.

Finally, I communicate the proposed prioritisation to get stakeholder buy-in. I revisit priorities regularly as new information or requirements emerge. This approach keeps the team focused on the most valuable work, helps avoid unnecessary rework, and ensures priorities remain aligned with project goals.

___

### 12. Give an example of when you took initiative or leadership in a project. / How would you handle incomplete or changing requirements in a project?

Project references: Oman FM

On one project the “nearest embassy” logic was undefined. I documented options, but that slowed decisions, so I organised a face-to-face meeting with the client and project team. Bringing decision-makers together enabled a focused discussion of trade-offs.

Walking everyone through the trade-offs led to a quick clarification and a simple practical implementation. Development resumed with no further delay, and the client had confidence in the agreed approach.

It showed that bringing the right people together can be the fastest way to resolve ambiguous requirements. That initiative prevented prolonged indecision and kept the project on schedule.

___

### 13. How do you communicate complex technical concepts to non-technical stakeholders?

I focus on outcomes, use simple analogies and visuals, and avoid jargon. I start with why something matters to the user or business, then show a short diagram or analogy to explain the mechanism in plain language.

For example, explaining an ETL sync to non-technical stakeholders I called the website the “source of truth” and compared updates to a news feed refresh, then showed a simple diagram of the flow. That kept the discussion on user impact rather than technical detail and enabled quick alignment.

This approach speeds decisions, reduces follow-up clarifications, and helps teams prioritise what drives user value.

___

### 14. Have you ever disagreed with a manager’s decision? What did you do?

My manager proposed splitting boilerplate into multiple repos and automating admin-page generation. I raised operational concerns — extra CI, secrets and limited practical benefit — and presented examples where modularisation helps. I framed my feedback as trade-offs rather than opposition.

I respected the decision, helped implement it, and suggested a pilot approach so we could test value with limited risk. The initiative was later dropped, but the process taught me to present trade-offs clearly and propose measurable pilots before wide adoption.

The experience reinforced the value of respectful disagreement, evidence-based recommendations, and pragmatic pilots to inform larger decisions.

___


### 15. How do you ensure you stay current with new technologies?

I combine courses, community and hands-on practice. Recently I’ve completed courses in Django, Node.js, microservices, Python for data science, NoSQL, ETL, containers, observability, application security and generative AI. Studying broadly helps me spot useful patterns and trade-offs.

I attend meetups and conferences, browse GitHub and Reddit, and set aside time for focused projects — for example an ETL pipeline or an AI demo — so I apply learning immediately. Hands-on projects convert theory into assets the team can reuse.

I also share findings with peers through pair programming and talks. Sharing accelerates team learning and helps validate whether a new tech actually improves outcomes.

___


### 16. Where do you see yourself in 5 years?.

In five years I see myself as a senior or lead full-stack engineer owning end-to-end features and helping shape technical direction. I want to be shipping scalable systems — particularly AI integrations — while mentoring others and improving engineering practices across the team.

I plan to combine hands-on delivery with a focus on coaching, design reviews, and observability so the systems I own are reliable and the team can move faster. Ultimately, I want to be in a role where I can both deliver high-impact work and amplify others’ contributions.

That vision guides my learning priorities today and keeps my efforts aligned with building sustainable, measurable outcomes for the organisation.

___


### 17. What motivates you at work?

I’m motivated by solving meaningful problems that deliver business value, learning new technologies, and collaborating with others. Turning an idea into a production feature that actually helps users is especially rewarding and often leads to follow-up improvements.

Seeing measurable user impact and team growth keeps me engaged. I enjoy projects where I can both produce code and help improve processes or documentation so the team benefits long-term.

That combination of tangible user outcomes, continuous learning, and peer collaboration drives my daily work and career choices.

___


### 18. How do you maintain work-life balance?

I set clear boundaries, prioritise work so I focus on the highest-value tasks during the day, and make time for exercise and recovery. Those habits help me maintain consistent performance without burnout.

I also communicate capacity with the team so we plan realistically — and when peaks happen I schedule recovery time afterwards. That ensures short-term intensity doesn’t become chronic stress.

By treating balance as an operational issue (planning, communication, recovery) I keep energy and focus sustainable while delivering reliably for the team.

___


### 19. Describe a time you had to learn something quickly to complete a task.

Project references: ACF

I needed to add GraphQL to an admin portal fast. I took a short course on GraphQL fundamentals, then built a quick prototype using Apollo Server with Express to learn schemas, resolvers and request flow. The prototype let me experiment without risking the main codebase.

I applied that pattern to the codebase, mapped data structures to GraphQL types, added resolvers and tests, and documented the model. That made the change maintainable for future developers and reduced onboarding friction.

That let me deliver the functionality within the deadline and hand over maintainable code. Rapid, focused learning plus an isolated prototype is my go-to approach for time-pressured upskilling.

___

### 20. How would your colleagues describe you?

References: Eleni, Jordan, Audrius

Colleagues would describe me as dependable, detail-focused and collaborative — someone who raises the bar on quality while being easy to work with. I try to be the person others can rely on when a problem gets tricky.

They’d say I’m logical, calm under pressure, and willing to mentor others. As one colleague put it, “Steven is a great presence to have around.” I value that reputation because it reflects both technical competence and team-minded behaviour.

I work to maintain that perception by being consistent, communicative, and focused on outcomes that help the team succeed.

___


### 21. Describe a time you collaborated with others to overcome a challenge.

Project references: Bare Dating

During the Bare Dating project, the client decided to bring development in-house and hired a new developer to take over the application. My role was to ensure the transition was smooth and that they could run the system independently.

I prepared a concise handover pack covering the architecture, deployment steps and environment setup, then walked through the codebase with them and performed a deployment together so they could see the process end to end. I stayed available to answer questions during the transition period.

After supporting their first releases and answering questions, the developer was able to manage deployments independently and the handover completed without disruption. The outcome preserved service continuity and reduced the client’s operational risk.

