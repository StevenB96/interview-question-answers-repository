_Italics = Reflection_

1. Tell me about yourself. (Give a concise personal introduction).

Hi, I’m Steven — a full-stack developer with three years’ commercial experience in a consulting environment and a master’s in engineering.

I’ve delivered end-to-end web and mobile solutions for small and medium businesses, working across API design, databases, frontend development, and deployment.

Recently, I took a focused career break to deepen my expertise in cloud services, generative AI, and modern frameworks, building hands-on projects to apply those skills in practice.

I’m now looking to join a team where I can take ownership of features end-to-end and help deliver scalable, user-focused products, including thoughtful AI integrations where appropriate.


2. Why do you want to be a software/full-stack developer?. 

I became a full-stack developer because software combines everything I enjoy about engineering: problem solving, systems thinking, and fast feedback loops.

My background exposed me to several engineering disciplines, but software offered the fastest way to prototype solutions and measure real-world impact.

In my previous role, I led the development of a UX demo feature that reduced customer queries about app usage by 31%, and I built an ETL pipeline that removed the need for manual data transformation and syncing.

I enjoy collaborating across teams to turn customer needs into robust, scalable code, and I’m keen to apply that experience to building user-focused products here.


3. What are your greatest strengths and weaknesses?.

Strengths

* Commitment to continous development.

One of my key strengths is a strong commitment to continuous development. I actively seek feedback and use it as a trigger for structured learning and improvement.

I regularly attend industry events such as Postman Developer Events, React Advanced Conference, and Django London Meetups to stay current with emerging tools and practices. I see technological change as an opportunity to add value and gain an edge.

* Team intergration.

Another strength is team integration. I bring positive energy without being overbearing, and I make deliberate effort to build relationships — even in remote environments. 

In my previous role, I initiated informal virtual lunch sessions to strengthen team cohesion. A colleague once described me as “a great presence to have around,” which reflects how I approach collaboration.

Weakness

* Overthinking challenges too early / worrying unessarily.

One area I’ve worked on is over-analysing problems too early. I sometimes research deeply before validating assumptions with teammates, which can waste time. For example, early on a project I spent several hours investigating a requirements issue before checking with the team; a quick alignment would have led to a faster resolution.

_To improve I now sanity-check my understanding with a colleague first, and time-box initial research (e.g., 30–60 minutes). That balance of quick validation plus focused follow-up research has noticeably reduced wasted effort._
 
* Judging whether to document of not.

I sometimes struggle to judge how much to document. Good documentation is valuable for handovers and complex systems, but over-documenting can slow delivery. On my last project I produced four interaction diagrams (one per module) for an AI risk-mitigation feature — that helped me, but I realised some artifacts were more detailed than necessary.

_To improve I now apply a lightweight rule: document for intent and interfaces (env vars, key data entities, sequence overview) and prefer short diagrams or READMEs over long docs. I also add a quick owner and review date so documentation stays useful and doesn’t become stale._


4. Describe your biggest professional achievement to date.

Project references: Oman Foreign Ministry

My biggest professional achievement was leading the development of a mobile app and admin portal from inception through the delivery of stage one. The product complemented their existing website and required UX design, maps/geolocation, push notifications, WordPress integration, and multi-language support.

I translated stakeholder needs into a prioritised backlog, estimated and delegated tasks, designed a resilient data model and ETL pipeline that handled tricky edge cases, and coordinated a small team (one junior developer and a junior project coordinator) via Scrum, paired programming and code reviews.

We delivered the first stage successfully; the client commissioned follow-on work, and both junior team members became productive contributors. The project demonstrated my ability to own both the technical design and team delivery end-to-end.


5. What is the hardest problem you’ve solved, and how did you solve it?.

Project references: obs-etl-k8s-demo-project

During a project designed to practice deployment, monitoring, and ETL offline, my Airflow container failed to start and a dependent service also broke, which blocked progress. Since I was the only developer, I owned the investigation end-to-end. 

I started by checking container logs and found errors hinting at a Redis/version mismatch, so I tried forcing a specific Redis version via an environment variable — that changed the symptoms but didn’t fix the startup. 

I then researched GitHub/Stack Overflow and used LLM tools to explore causes, and tried a couple of config changes like limiting the deployment to a single node, but those didn’t help. 

Finally I audited the container images and tags and discovered the upstream images were no longer available in the way I expected; the project recommended migrating to a community (libre) image. After switching to the community image the deployment succeeded and development continued.

The difficulty in debugging this issue was that it wasn’t documented online, and the logs provided very little information. Resolving it would have required deep knowledge of the Prometheus image, which I didn’t have. However, by systematically eliminating potential causes, I eventually discovered a source that indicated the correct solution.


6. Tell me about a time you failed or received criticism and what you learned.

Project references: Barnfield Caravans

Early in my career, I worked on an admin portal where we had a repetitive pattern for implementing form fields. Because I could see all the requirements upfront, I decided to implement most of them at once rather than strictly following the ticket sequence. My intention was to work more efficiently and ensure we met the overall milestone.

However, I underestimated the impact this would have on project visibility. The client had access to the Kanban board, and when the first ticket overran its estimate it reduced their confidence in the project timeline. Because the project was lower priority internally, this wasn’t corrected quickly enough, and the client eventually decided to stop the work.

I received feedback that I should have raised the idea with stakeholders before deviating from the ticket structure. The key lesson for me was that transparency and alignment are just as important as technical efficiency.

_Since then, if I think a different implementation approach could improve delivery, I discuss it with the team first and adjust the backlog together rather than making that decision alone._


7. How do you handle tight deadlines or stressful situations?

Project references: Bare Dating

When working under tight deadlines or stressful situations, I focus on three things: prioritisation, breaking work into manageable tasks, and clear communication.

First, I identify the most important deliverables so the team focuses on the work that provides the most value. Then I break the work into smaller tasks so progress can be tracked and potential issues can be identified early. Throughout the process, I keep communication frequent so expectations stay aligned and blockers are addressed quickly.

For example, on one project, the client publicly announced upcoming features before development was complete, which created pressure around delivery timelines. In response, we made sure to keep the client closely updated on progress and realistic delivery expectations. By prioritising the key features and maintaining clear communication, we were able to manage the situation effectively and keep the project moving forward without surprises.


8. Give an example of working effectively under pressure.

Project references: Alternative Commercial Finance

Early in my career I was handed a high-pressure project to extend an application — essentially a “poison-chalice” task. I was the primary developer (with a senior lead overseeing) and had to deliver the bulk of features, plus reverse-engineer the business domain from code because database migrations couldn’t be run.

The technical challenges were significant. I needed to extend an unfamiliar codebase using Node.js and GraphQL, understand architectural patterns I hadn’t worked with before, and reconstruct the entity-relationship model directly from the code. Along the way I also encountered unexpected debugging issues, including Java/Jasper runtime errors and SQL compatibility problems. In addition, communication was challenging because the customer had limited documentation and only partial knowledge of their own business processes.

My approach combined learning, investigation, and communication. I took focused online courses to quickly upskill on Node.js and GraphQL, instrumented the codebase to trace data flows, and produced an ERD and a short report explaining the domain model. I pushed for face-to-face sessions with the customer to validate assumptions and walked the project team through my findings.

As a result I delivered the agreed features and a clear domain report so the team could continue development without me. Although the client’s long-term resourcing meant we couldn’t continue at the desired pace, the immediate deliverables were shipped and the team was left with the documentation and diagrams needed to move forward. _I learned to combine rapid technical learning with structured investigation and proactive stakeholder communication when working solo under pressure._


9. Describe a conflict you had with a teammate and how you resolved it.

I was reassigned to a project in order to maintain a module where a database calculation had recently been refactored into a large pure-SQL query. The change had no explanatory log or test, and I wasn’t comfortable working with it in that state.

I needed to understand and maintain that calculation, and ensure it remained correct and maintainable for future development.

I spoke with the developer who made the change. He explained the SQL reduced execution time; I explained my concerns about readability and maintainability, and asked whether the improvement had been measured in the context of the whole feature. We debated our approaches — both valid — and then I pointed out that I was now responsible for that functionality and needed a version I could work with. He reluctantly agreed to let me revert to the previous implementation on the main branch. To reach a durable compromise I proposed and implemented a follow-up plan: I incorporated the raw SQL in a more idiomatic way (for example, wrapping it in a well-documented database function).

We kept the performance benefit available while making the code understandable and testable for future maintainers. _The situation taught me the value of combining evidence (benchmarks, tests) with clear documentation and of negotiating pragmatic compromises when ownership changes._


10. How do you receive and act on feedback?

Project references: ai_tool-risk_mitigation-demo-project, obs-etl-k8s-demo-project

I welcome feedback and treat it as a practical prompt for improvement. I always thank the person giving the feedback, evaluate it, and turn it into an action plan — often with hands-on work that I can validate.

Recently I received two distinct pieces of feedback from interviews: first, that I needed more exposure to user-centric and production debugging patterns; second, that I should present more concrete, impact-focused examples of my work. To address those directly I created two targeted projects.

The first was an Observability & ETL demo (Airflow + Kafka + Prometheus/Grafana + Jaeger on kind) to practise deployment, monitoring and diagnosing pipeline issues end-to-end. I set clear success criteria — end-to-end deployability, working dashboards and a runbook — and validated the work by running smoke tests and walking peers through the runbook.

The second was an interview Q&A repository and a secure AI integration demo to produce demonstrable, impact-focused examples I can show in interviews. For both projects I sought follow-up feedback from experienced reviewers and iterated based on their suggestions.

_In short: I listen, plan, act and validate — turning feedback into measurable learning and tangible artefacts I can demonstrate._


11. How do you prioritise tasks when given multiple priorities?

I prioritise work by combining a simple framework (value vs effort) with pragmatic checks for deadlines, blockers and dependencies — and I keep stakeholders involved throughout.

* Value / effort first.
I score each task on expected value (impact to users or business) and required effort (time, risk). High-value, low-effort items get top priority. This gives a quick, rational baseline for decisions.

* Respect hard deadlines.
If a task has a fixed deadline (e.g. a public demo) it usually moves to the top of the queue. If a deadline looks unrealistic I raise it early and propose a more feasible plan.

* Check blockers and resources.
I ask whether any task is blocked (waiting on credentials, a third-party, or a subject-matter expert). Unblocked work that can progress immediately often gets higher priority than blocked but higher-value items.

* Consider dependencies and combined value.
Sometimes tasks are synergistic — grouping them reduces duplicated effort or reduces context switches. I evaluate whether completing related tasks together increases net value or lowers overall effort.

* Communicate and negotiate.
Prioritisation is rarely a solo decision. I share my proposed ordering with product owners and engineers, explain the trade-offs (value, effort, risk), and adjust based on business priorities. That alignment reduces surprises later.

* Re-evaluate regularly.
I keep priorities visible (Kanban board or backlog) and review them daily/weekly depending on cadence. New information — a production incident, new customer input, or a changed deadline — triggers a quick re-prioritisation.


12. Give an example of when you took initiative or leadership in a project.

Project references: Oman Foreign Ministry

On one project, I was working on a mobile application that included functionality to show users their nearest embassy or consulate. When I began implementing it, I realised the requirements were incomplete — the logic for determining the “nearest” location wasn’t specified, and different interpretations could produce different results.

To move things forward, I first analysed the problem and wrote a short document outlining the ambiguity and proposing several possible approaches. However, when I shared it with the team it became clear the written explanation was a bit overwhelming and slowing the decision process.

So I took the initiative to organise a face-to-face discussion with both the project team and the customer. In the meeting I walked them through the core decision points and the trade-offs between the options. Once we were all aligned in the same room, the customer quickly clarified the intended behaviour and we agreed on a simple, practical implementation.

The outcome was that the ambiguity was resolved quickly, development continued without further delays, and we avoided implementing the wrong logic. _It reinforced for me that when requirements are unclear, sometimes the most effective leadership is bringing the right people together to make a decision quickly._


13. How do you communicate complex technical concepts to non-technical stakeholders?

When communicating complex technical concepts to non-technical stakeholders, my goal is to focus on the business outcome rather than the technical implementation. I usually translate technical ideas into simple analogies, visual diagrams, or step-by-step explanations that relate directly to the problem the stakeholder cares about.

For example, on a project where we were building a mobile application that integrated with a WordPress content system, we needed to explain how an automated data pipeline would synchronise content between the website and the mobile app. The technical implementation involved APIs, data transformation, and scheduled background jobs, which could easily sound complicated.

Instead of focusing on those details, I explained it using a simple analogy: the website would act as the “source of truth”, and the app would receive regular automated updates — similar to how a news feed refreshes periodically. I also created a simple diagram showing the flow of information from the website, through a processing step, and into the app’s database.

By keeping the explanation visual and focused on the outcome — reliable, up-to-date content in the app — the stakeholders were able to quickly understand the system and approve the approach without needing to understand the underlying technical details.


14. Have you ever disagreed with a manager’s decision? What did you do?

In one situation I disagreed with my line manager about an initiative to split our boilerplate into multiple repositories and build an automated admin-portal generator. My concern was that the proposed modularisation would add repo/secret management overhead without delivering much value, because the modules wouldn’t be deployed or used as independent services — they’d still be integrated tightly in the app. I also worried the automated generator would make handling edge cases more challenging.

I raised these points with examples: I explained where modularisation helps (when a module is an independent service or has its own data/API) and where it doesn’t, and I demonstrated potential operational costs (extra CI/CD, secret scopes, repo linking). I recognised my manager’s authority and the value of the proposal, so after discussing my concerns I supported the implementation and helped with the rollout.

The initiative was later discontinued, but the process was valuable: I learned how to present trade-offs respectfully, back arguments with concrete examples, and balance advocacy with team alignment. _Going forward I try to propose a small pilot or proof-of-concept and quantify the operational cost before asking the team to adopt a big change._


15. How do you ensure you stay current with new technologies? (Learning habits)

I treat staying current as a deliberate, multi-channel habit rather than something that happens by accident. I combine structured learning, community engagement and hands-on practice.

For structured learning, I regularly take targeted courses to deepen my understanding of key areas. Recently I’ve completed courses in Django development, Node.js, microservices and serverless architecture, Python for data science, NoSQL databases, ETL and data pipelines, containers such as Docker and Kubernetes, monitoring and observability, application security, and generative AI development with Python.

Alongside that, I attend conferences and meetups — for example events focused on React, Django and Next.js, as well as vendor sessions such as Postman talks — to see how engineers are solving real problems and to learn practical patterns. I also browse GitHub and communities like Reddit to see what tools and libraries people are actively using in real projects.

On the practical side, I set aside time for short, focused projects where I apply what I’ve learned. For example, building small ETL pipelines, observability demos, or AI integrations helps me move from theory into real implementation.

Finally, I learn a lot through collaboration — discussions with colleagues, pair programming, and informal knowledge-sharing sessions are great ways to exchange ideas and gain feedback on new technologies.


16. Where do you see yourself in 5 years?.

In five years I see myself as a senior or lead full-stack engineer delivering end-to-end features and helping guide technical direction. I’d like to be building scalable systems, particularly those involving AI integrations, while mentoring other engineers and contributing to strong engineering practices within the team.


17. What motivates you at work?

I’m motivated by solving meaningful problems that deliver real value to the business, while continuing to learn new technologies and collaborate with others. I particularly enjoy seeing a feature move from idea to implementation and then being used in production. Knowing that something I built is helping users or improving a workflow is very satisfying, and it often leads to further ideas and opportunities to improve the product.


18. How do you maintain work-life balance?

I maintain work–life balance by setting clear boundaries and prioritising my work so I can focus on the most important tasks during the day. I also make time for exercise and recovery, which helps me stay productive and focused. I try to communicate openly with my team about capacity and priorities so we can plan work realistically and avoid unnecessary pressure.


19. Describe a time you had to learn something quickly to complete a task.

Project references: 2PD

I once needed to add GraphQL functionality to an administration portal, but I hadn’t used GraphQL in production before and the timeline was tight.

To learn it quickly, I took a short course on GraphQL fundamentals and built a small prototype using Apollo Server with Express. That helped me understand schemas, resolvers and how requests map to backend logic.

I then applied that pattern to the existing codebase by mapping the project’s data structures to GraphQL types and implementing resolvers that connected the schema to the application logic.

This allowed me to deliver the required functionality and also document the domain model so the team could more easily continue developing features.

20. How would your colleagues describe you?

References: Eleni, Jordan, Audrius

My colleagues would describe me as a dependable, detail-focused engineer who raises the bar on quality while being easy to work with. 

They’d say I’m logical and solution-oriented — someone who isn’t afraid to challenge the team constructively to improve requirements — and who stays calm under pressure. 

I also mentor others and make time to build team cohesion: as one teammate put it, “Steven is a great presence to have around,” and another noted that I “helped challenge the team… and suggest creative solutions to complex problems.” 

Overall I’m seen as a proactive, collaborative engineer who delivers solid, maintainable work and helps others do the same.