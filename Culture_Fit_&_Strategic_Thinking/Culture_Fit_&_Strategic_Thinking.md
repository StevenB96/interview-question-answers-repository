# Problem Solving & Scenario Based Questions

___

### 1. What do you think you can contribute to our team outside of coding?

Outside of coding, I contribute through collaboration and knowledge sharing. I enjoy helping teammates think through technical problems, reviewing code thoughtfully, and sharing useful tools or learning resources. I make a point of turning ad-hoc learnings into shareable artifacts so knowledge scales beyond one-on-one conversations.

I also try to contribute to a positive team culture. I make a deliberate effort to build strong working relationships and encourage open discussion during problem-solving. That attention to culture reduces friction and helps the team reach consensus faster when decisions are needed.

For example, I’ve organised informal knowledge-sharing sessions and virtual lunch meetups to help maintain team cohesion, particularly in remote environments. Those sessions help surface recurring questions and accelerate onboarding, which ultimately lets the team spend more time delivering features.

___

### 2. How do you stay motivated when working on tedious tasks?

When I’m working on a tedious task, I try to focus on the value it delivers rather than the repetition itself. I remind myself how the task contributes to the larger goal — whether that’s improving system reliability, enabling another feature, or removing manual work later. Framing the work this way keeps the end benefit visible and makes the task feel purposeful.

Practically, I break the work into smaller steps so I can maintain momentum and see progress. I’ll sometimes use small techniques like listening to music or taking short breaks to stay focused, but I often find that once I get into the flow of the task, the work becomes much more engaging and the sense of progress keeps me motivated. I also treat repetitive tasks as opportunities to identify automation potential.

When I spot automation opportunities I prototype a small script or pipeline that eliminates recurring manual effort. Over time this approach reduces repetitive work for the team and increases the time available for higher-value engineering.

___

### 3. What is your ideal team culture, and how do you fit into it?

My ideal team culture is collaborative, supportive, and focused on continuous improvement. I value teams where people feel comfortable asking questions, sharing ideas, and giving constructive feedback. In that environment, engineers can learn from each other and build better solutions.

I try to contribute to that culture by being approachable, communicating clearly, and helping others when I can — whether through code reviews, pairing sessions, or sharing knowledge. I make a deliberate effort to give feedback that’s specific and actionable so reviews become teaching moments rather than gates.

I also work to create opportunities for low-risk experiments and retrospectives so the team can iterate on process and technical approaches. That approach helps the team improve predictably over time while keeping morale high.

___

### 4. Describe how you prioritise your personal development.

I prioritise personal development by focusing on areas that are both interesting and relevant to the systems I’m working on. I also pay close attention to feedback from colleagues and interviews, using it to identify skills or gaps that will have the most impact on my work. That keeps learning practical rather than purely theoretical.

This approach ensures my development is targeted, practical, and aligned with both my growth and the team’s needs. I set small, achievable goals and combine hands-on practice with curated learning resources so I can apply new skills quickly.

I also seek mentorship and try to apply new techniques directly to production problems, which helps me verify value and adjust priorities. Over time this keeps my contributions aligned with what the team actually needs rather than what’s simply interesting.

___

### 5. How would you handle a situation where priorities change suddenly?

When priorities change suddenly, my first step is to understand the new goal and how it affects the current work. I review what tasks are in progress, identify what can be paused or adjusted, and clarify the most important deliverables with the team or project lead. That quick clarity prevents wasted effort on low-priority work.

Then I communicate any risks or timeline impacts early. I update stakeholders with a short summary of trade-offs, revise estimates, and reassign or reprioritise tasks as required. I also make sure paused items are captured with context so resuming them later is straightforward.

Staying flexible while keeping communication clear helps ensure the team can adapt quickly without losing track of important work. This minimises rework and helps leadership make informed trade-offs that preserve business value.

___

### 6. How do you balance short-term deadlines with long-term project goals?

I balance short-term deadlines with long-term goals by combining prioritisation with strategic planning. I use a value-versus-effort approach to identify high-impact tasks that are quick wins, but I also respect deadlines and adjust priorities when necessary. That lets us deliver immediate value without losing sight of the architecture.

I check for blockers and dependencies, and group related work to reduce duplicated effort. When quick solutions are needed, I make them modular and document assumptions so future improvements are easier. I also capture technical debt as explicit tickets with owners and timelines to ensure it doesn’t become forgotten.

Clear communication with the team ensures short-term decisions don’t create long-term problems. By treating short-term work as part of a larger roadmap, we preserve velocity while keeping the system maintainable.

___

### 7. Describe a strategic change you would recommend for a project or product.

One strategic change I often recommend is improving observability. On many projects, diagnosing issues can be slow because there isn’t enough visibility into system behaviour. By adding monitoring, structured logging, and dashboards for key metrics like error rates and response times, teams can identify problems earlier, diagnose issues faster, and make more informed decisions about performance and reliability.

Essentially, I focus on collecting logs, system metrics, and traces to give the team full visibility into how the system is behaving in real time. I recommend rolling this out incrementally — instrument critical paths first, create actionable dashboards, and build runbooks to ensure alerts translate to quick remediation.

This approach shortens incident diagnosis, reduces user impact, and makes it easier to prioritise engineering effort based on measurable system health rather than guesswork.

___

### 8. Tell me about a time you initiated a process improvement.

Project reference: LLL

While working on a project, I noticed that code reviews were quite inconsistent. Sometimes reviewers focused on style, while other times they focused on architecture or implementation details. Without a shared framework, the outcome of a review could vary significantly between developers or projects.

To improve this, I suggested introducing a lightweight code review checklist covering tests, edge cases, security considerations, performance, and documentation. I also proposed a simple severity key so reviewers could distinguish between critical issues and personal preferences, helping keep feedback constructive. I then created a short pull request template incorporating these guidelines so reviewers had a consistent structure to follow.

As a result, review quality became more consistent across projects, onboarding new developers became easier, and the team experienced less back-and-forth during reviews. The change turned subjective reviews into repeatable practice and reduced friction in the merge process.

___

### 9. Give an example of a difficult decision you made in a past project.

Project reference: 2PD

On the project, I needed to decide how we should host the application on AWS while keeping in mind the constraints typical for an SME — limited infrastructure resources and the need for a simple deployment process. I evaluated three options: hosting directly on EC2, which gives full control but requires managing servers; using a container platform like ECS or Kubernetes, which offers scalability but adds operational complexity; and using a managed platform such as Elastic Beanstalk.

I recommended Elastic Beanstalk because it provided the best balance between reliability, scalability and low operational overhead. It allowed us to deploy quickly while AWS handled much of the infrastructure management, which meant the team could focus more on delivering features rather than maintaining servers. To make the choice safer I added monitoring and clear rollback runbooks so we could detect and respond to issues quickly.

The result was smoother deployments and less operational distraction for the engineering team, enabling faster feature iteration under the SME constraints we had to respect.