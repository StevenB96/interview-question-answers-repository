# Problem Solving & Scenario Based Questions

___

### 1. What do you think you can contribute to our team outside of coding? ✔

Project reference: ACF

Outside of coding, I contribute through collaboration and knowledge sharing. I enjoy helping teammates think through technical problems, reviewing code thoughtfully, and sharing useful tools or learning resources. I make a point of turning ad-hoc learnings into shareable artifacts.

**For example**, on a project (codename ACF) I had to debug SQL syntax issues. My solution was to implement a flexible database driver package. Subsequently, this I updated the knowledge base and the boilerplate code.

I also try to contribute to a positive team culture. I make a deliberate effort to build encourage open discussion during problem-solving and strong working relationships. That attention to culture reduces friction and helps the team reach consensus faster when decisions are needed.

**For example**, I’ve organised informal knowledge-sharing sessions and virtual lunch meetups to help maintain team cohesion, particularly in remote environments.

___

### 2. How do you stay motivated when working on tedious tasks? ✔

Project reference: LLL

When I’m working on a tedious task, I try to focus on the value it delivers rather than the repetition itself. I remind myself how the task contributes to the larger goal — whether that’s improving system reliability, enabling another feature, or removing manual work later. Framing the work this way keeps the end benefit visible and makes the task feel purposeful.

**For example**, on a project (codename LLL) I decided to refactor the React codebase from class commponents to functions and hooks. This was a necessary change, but a highly repetitive task. Throughout I kept in mind the benefits: simplicity, reusabilty, performance, etc.

Practically, I break the work into smaller steps so I can maintain momentum and see progress. **For example**, I was a able to breakdown the work by component heirachies e.g. screens -> containers -> elements -> components -> etc.

I’ll sometimes use small techniques like listening to music or taking short breaks to stay focused, but I often find that once I get into the flow of the task, the work becomes much more engaging and the sense of progress keeps me motivated. 

I also treat repetitive tasks as opportunities to identify potential for reusability or automation. **For example**, I while I was refactoring the code, I noticed that the screen size variable was required on multiple screens, so I abstracted it into a hook and updated the knowledge base and the boilerplate code.

___

### 3. What is your ideal team culture, and how do you fit into it? ✔

Project reference: N/a

My ideal team culture is collaborative, supportive, and focused on continuous improvement. I value teams where people feel comfortable asking questions, sharing ideas, and giving constructive feedback. In that environment, engineers can learn from each other and build better solutions.

I try to contribute to that culture by being approachable, communicating clearly, and helping others when I can — whether through code reviews, pairing sessions, or sharing knowledge. I make a deliberate effort to give feedback that’s specific and actionable so reviews become teaching moments rather than gates.

I also work to get stakesholder buy in for learning oppertunities, low-risk experiments and retrospectives so the team can iterate on process and technical approaches. That approach helps the team evolve ideas over time while keeping morale high.

___

### 4. Describe how you prioritise your personal development. ✔

Project reference: ai_tool-risk_mitigation-demo-project

I prioritise personal development by focusing on areas that are both interesting and relevant to the systems I’m working on. I also pay close attention to feedback from colleagues and interviews, and seek mentorship. This helps me to keep my contributions aligned with what the team actually needs rather than what’s simply interesting. 

**For example**, after reaching the interview stage for a recent job application, I asked if there were specific topics they'd like to discuss. They wanted to focus on AI integrations relevant to their business, so that I could focus my preperation 

Then I set small, achievable goals and combine hands-on practice with curated learning resources so I can apply new skills quickly. I also try to apply new techniques directly to production problems, which helps me verify value and adjust priorities. This approach ensures my development is both theoretical and practical.

**For example**, in response to their feedback, I created an "ai_tool-risk_mitigation-demo-project," dividing it into manageable work packages and combining documentation review with coding to develop a user-friendly web server that demonstrates my hands-on skills.

___

### 5. How would you handle a situation where priorities change suddenly? ✔

Project reference: BD

When priorities change suddenly, my first step is to understand the new goal and how it affects the current work. I review the tasks already in progress and identify what can be paused, adjusted, or continued so the team can focus on the highest-value work.

**For example**, on a project (codename BD), the client’s crowdfunding resources were starting to run low, so they asked us to prioritise delivering packages related to the platform’s essential functionality. I reviewed the backlog and current work and found a high-effort, medium-value game feature in development, several essential packages still pending, and multiple bug fixes at different stages of the development lifecycle.

Then I update stakeholders with a short summary of the trade-offs and clarify the most important deliverables. I also make sure paused work is documented with enough context to resume later. This approach helps the team adapt quickly while keeping delivery focused on the most critical functionality.

**For example**, following discussion, we paused the game feature but continued work on the bug fixes and essential packages, in that order.

___

### 6. How do you balance short-term deadlines with long-term project goals? ✔

For my general prioritisation approach, please see **“How do you prioritise tasks when given multiple priorities?”**.

If a short-term deadline conflicts with long-term project goals, I first assess whether the immediate requirement is truly time-critical or whether there is flexibility in scope or delivery. When a quick solution is needed, I aim to keep it modular and document assumptions so that future improvements or refactoring are easier. I also capture any technical debt as explicit tickets with owners and tentative timelines so it doesn’t become forgotten.

Clear communication with the team helps ensure short-term decisions don’t create long-term problems. By treating short-term work as part of a larger roadmap, we preserve delivery momentum while still keeping the system maintainable and easier to evolve over time.

___

### 7. Describe a strategic change you would recommend for a project or product. ✔

Project reference: obs-etl-k8s-demo-project

One strategic improvement I often recommend is adopting a microservice architecture deployed on a container orchestration platform such as Kubernetes. This provides key operational capabilities including automated deployment, service discovery, fault isolation, horizontal scaling, and strong observability when integrated with monitoring and tracing stacks (e.g., Prometheus and OpenTelemetry).

**For example**, this approach is demonstrated in my project obs-etl-k8s-demo-project. In this implementation, I containerised a Python Flask application and deployed it to a Kubernetes cluster using a declarative infrastructure-as-code approach. Kubernetes manages the lifecycle of the service, using internal DNS-based service discovery and readiness probes to ensure reliable routing of network traffic between components. To support the observability capabilities described above, the project integrates a full monitoring and tracing stack. The Flask application uses OpenTelemetry to export distributed traces to a centralised Jaeger instance, while application and system metrics are scraped by Prometheus via a ServiceMonitor.

Together, these components transform a simple application into a resilient, observable, and scalable system where developers can trace the journey of a single transaction and operate distributed services with the visibility required to scale safely.

___

### 8. Tell me about a time you initiated a process improvement. ✔

Project reference: LLL

While working on a project (codename LLL), I noticed that code reviews were quite inconsistent. Sometimes reviewers focused on style, while other times they focused on architecture or implementation details. Without a shared framework, the outcome of a review could vary significantly between developers or projects.

**To improve this**, I suggested introducing a lightweight code review checklist covering tests, edge cases, security considerations, performance, and documentation. I also proposed a simple severity key so reviewers could distinguish between critical issues and personal preferences, helping keep feedback constructive. I then created a short pull request template incorporating these guidelines so reviewers had a consistent structure to follow.

As a result, review quality became more consistent across projects, onboarding new developers became easier, and the team experienced less back-and-forth during reviews. The change turned subjective reviews into repeatable practice and reduced friction in the merge process.

___

### 9. Give an example of a difficult decision you made in a past project. ✔

Project reference: PB

While working on a project (codename PB), I was tasked with integrating OAuth into our boilerplate to broaden our security offerings. The primary decision was whether to adopt a vendor solution or build a custom OAuth system.

For my general prioritisation approach, please see **“How do you decide if a solution is the best approach to a problem? (Weighing pros/cons)”**. 

I compiled a list of relevant trade-offs, including:
> Flexibility — As a software house with a diverse client base, it was important to support a range of client requirements.
> Security — Security is a critical consideration for any authentication system.
> Maintainability — We needed the ability to maintain, fix, and improve the solution over time.
> Time / cost — As this was relatively low-priority work, it was preferable to choose a solution that could be implemented quickly.

Scoring both approaches against the criteria led to the following conclusions:
> Flexibility — A custom OAuth system offers greater flexibility, especially for multi-step authentication and device linking, since most projects involved mobile, web, and backend apps.
> Security / Compliance — Both approaches can be made secure. Vendors typically provide a faster, higher level of security out of the box, but a custom solution better supports compliance needs for finance, healthcare, and government clients.
> Maintainability — Both approaches are similarly maintainable: vendor solutions introduce external dependencies and potential API contract issues, while a custom system requires ongoing code maintenance.
> Time / Cost — Vendors reduce development effort and time-to-market, but a custom solution can be more cost-effective for certain clients over the long term.

I chose the custom OAuth approach because flexibility and compliance were essential for most of our clients, while the other criteria were roughly balanced. I communicated the decision to stakeholders to secure buy-in, documented the reasoning, and put a fallback plan in place to adopt a vendor solution later if needed.