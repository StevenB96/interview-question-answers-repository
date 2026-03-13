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

For my general prioritisation approach, please see “How do you prioritise tasks when given multiple priorities?”.

If a short-term deadline conflicts with long-term project goals, I first assess whether the immediate requirement is truly time-critical or whether there is flexibility in scope or delivery. When a quick solution is needed, I aim to keep it modular and document assumptions so that future improvements or refactoring are easier. I also capture any technical debt as explicit tickets with owners and tentative timelines so it doesn’t become forgotten.

Clear communication with the team helps ensure short-term decisions don’t create long-term problems. By treating short-term work as part of a larger roadmap, we preserve delivery momentum while still keeping the system maintainable and easier to evolve over time.

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