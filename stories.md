## Generated Story -5528322844687435599
* smalltalk.greetings.whatsup
    - utter_smalltalk.greetings.hello
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye 
* create.todolist
    - utter_ask_todo_list_name
    - action_create_todo_list
    - utter_askAnotherTaskToAdd

## Generated Story -6726550755041232838
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* smalltalk.greetings.how_are_you
    - utter_smalltalk.agent.good

## Generated Story 4021639759432779824
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* create.todolist
    - utter_ask_todo_list_name
* smalltalk.appraisal.thank_you{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - slot{"tolist-name": "my tasks"}

## Generated Story 8822779579396779268
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* create.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - slot{"todolist-task-name": "exercise"}
    
## Generated Story 6164533330224101518
* smalltalk.greetings.goodevening
    - utter_smalltalk.greetings.goodevening
* smalltalk.user.good
    - utter_smalltalk.agent.can_you_help
* create.todolist{"tolist-name": "daily tasks"}
    - slot{"tolist-name": "daily tasks"}
    - action_create_todo_list
    - slot{"tolist-name": "daily tasks"}
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "meditation"}
    - slot{"todolist-task-name": "meditation"}
    - action_add_task_to_list
    - slot{"todolist-task-name": "meditation"}
    - utter_askAnotherTaskToAdd
* create.todolist.addTask - yes
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - slot{"todolist-task-name": "exercise"}
* retrieve.todolist{"tolist-name": "daily tasks"}
    - slot{"tolist-name": "daily tasks"}
    - action_retrieve_todo_list
    - slot{"tolist-name": "daily tasks"}
* smalltalk.appraisal.thank_you
    - utter_smalltalk.agent.can_you_help
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye

## Generated Story -7333735099428243758
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* create.todolist{"tolist-name": "daily tasks"}
    - slot{"tolist-name": "daily tasks"}
    - action_create_todo_list
    - slot{"tolist-name": "daily tasks"}
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - slot{"todolist-task-name": "exercise"}
    - utter_askAnotherTaskToAdd
* create.todolist.addTask - no
    - utter_smalltalk.appraisal.thank_you

## Generated Story -96501441473873762
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye

## Generated Story -8145123694768262169
* Default Fallback Intent
    - utter_smalltalk.greetings.hello
* create.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "morning walk"}
    - slot{"todolist-task-name": "morning walk"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* create.todolist.addTask - no
    - utter_smalltalk.appraisal.thank_you

## Generated Story -8456087018500344832
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* create.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "morning walk"}
    - slot{"todolist-task-name": "morning walk"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* create.todolist.addTask - yes
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "meditation"}
    - slot{"todolist-task-name": "meditation"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* create.todolist.addTask - no
    - utter_smalltalk.appraisal.no_problem

