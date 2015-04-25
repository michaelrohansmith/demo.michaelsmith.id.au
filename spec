1. Imagine you have a project comprised of consecutive tasks A, B, C
    and D. Any task in the project will only become active when the
    preceding task has been completed,
    i.e. task B is inactive until task A has been has been completed,
    task C only becomes active on completion of B and so on. How would
    you model this? What kind of objects
    would you use or how would you lay out your database?
 2. Based on the model you described in 1, _implement your solution in
    Python, PHP or Node.JS (JavaScript/CoffeeScript) using any framework
    and/or libraries of your choice_.
    The implementation should also allow for the creation and display of
    the ordered tasks mentioned in 1 along with their status.
 3. Your project workflow has changed, so that every task becomes a two
    step process where every task first needs to be assigned to someone
    from a group of users
    before it can be completed. How do you change your model to allow
    for this new workflow? _You do not need to implement this in actual
    code._
 4. The assignee of task B has decided that he needs to create two new
    consecutive tasks E & F which he or she assigns to other users. He
    can only complete task B once
    these two tasks have been completed. The sub tasks should only ever
    be visible to the assignees of tasks B, E & F, i.e. the sub-tasks
    are fully transparent to all other
    participants of the main project. How would you adjust your model to
    achieve that?_You do not need to implement this in actual code._
 5. On completion of task C, a new project with consecutive tasks G, H &
    I is created which runs concurrently with the remainder of the
    current project (i.e. task D). How do
    allow for this? _You do not need to implement this in actual code.___
 6. How would you report on details like current status of project or
    assignee of current task? Describe your approach or write a pseudo
    query.
 7. The assignee of task A wants to be notified of completion of end
    tasks D and I. How do you achieve this without adding any new tasks?
    What other mechanism could you
    introduce? Describe an algorithm or write (pseudo) code to
    illustrate your approach. _You do not need to implement this in
    actual code.___
 8. How would you test your workflow representation? What would you test
    and how? _You do not need to implement this in actual code._
 9. What would it mean to your model if it needed to allow for
    insertion, removal or swapping of tasks? What would it mean in terms
    of algorithms?_You do not need to implement this in actual code._
10. How would you change your workflow for your tasks from assign ->
    complete to assign -> re-assign -> complete? _You do not need to
    implement this in actual code.
