import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.c = self.conn.cursor()
        self.create_task_table()
    
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name STRING NOT NULL,
            priority INTEGER NOT NULL
        );''')

        self.conn.commit()
    
    def find_task(self, name):
        stmt = '''SELECT name FROM tasks WHERE name = ?;'''
        prev_name = self.c.execute(stmt, (name,)).fetchone()
        return prev_name

    def show_task(self):
        stmt = '''SELECT id, name, priority FROM tasks;'''
        res_it = self.c.execute(stmt)
        head_key = ["ID", "TASK", "PRIORITY"]
        head_width = [5, 25, 5]
        for (k, w) in zip(head_key, head_width):
            print(k.ljust(w), end="")
        print()
        print("="*40)
        for (id, task, priority) in res_it:
            print(str(id).ljust(5), task.ljust(25), str(priority).ljust(5))

    def delete_task(self):
        task_id = int(input("Enter task id: "))

        stmt = '''DELETE FROM tasks WHERE id=?'''
        ret = self.c.execute(stmt, (task_id,))
        self.conn.commit()
        self.show_task()
        # print('deleted', ret.fetchone(), type(ret))
        
    
    def add_task(self):
        name = input("Enter a task: ")

        while not name.strip():
            name = input("Empty task. Please enter a task: ")

        priority = int(input("Enter a priority: "))
        while priority < 1:
            priority = int(input("Priority less than 1. Please enter positive integer."))

        prev_name = self.find_task(name)
        
    
        if not prev_name:
            self.c.execute('''INSERT INTO tasks (name, priority) VALUES (?, ?);''', (name, priority,))
            self.conn.commit()
        else:
            self.c.execute('''UPDATE tasks SET priority=(?) WHERE name=(?);''', (priority, name,))
            self.conn.commit()
        
        self.show_task()

    def change_priority(self):

        task_id = int(input('Enter task id: '))
        npriority = int(input("Enter priority: "))

        stmt = '''UPDATE tasks SET priority=(?) WHERE id=(?);'''
        self.c.execute(stmt, (npriority, task_id,))
        self.conn.commit()

        self.show_task()


    def exit_todo(self):
        exit()
    

    def display_menu(self):
        while True:
            m = input('Enter [A/a] for adding tasks.\nEnter [S/s] for displaying tasks.\nEnter [U/u] for updating tasks.\nEnter [D/d] for deleting tasks.\nEnter [E/e] for \exiting out of the app.\n')
            if m in ['a', 'A']:
                self.add_task()
            elif m in ['s', 'S']:
                self.show_task()
            elif m in ['u', 'U']:
                self.change_priority()
            elif m in ['d', 'D']:
                self.delete_task()
            elif m in ['e', 'E']:
                self.exit_todo()
            else:
                print("Not a valid option. Please try again.")

todo_app = Todo()
todo_app.display_menu()
# todo_app.add_task()
# todo_app.delete_task(5)
# todo_app.show_task()

