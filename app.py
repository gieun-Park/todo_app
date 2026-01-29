import streamlit as st

st.title('✔To-do App✔')

class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 리스트 안에 있을 때 리스트 안의 요소들을 출력하려면 repr을 사용(str은 출력 안 됨)
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

# repr은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는 게 원칙이다.
# return f'Todo(task="{self.__task}", done={self.__done})'
# return f'Todo(task={self.__task!r}, done={self.__done})'

# __repr__ 심화
# todo = Todo('숙제하기')
# print(id(todo))
# todo2 = eval(repr(todo))
# print(id(todo2))

# todo 객체를 list에 쌓는 용도의 함수(추가할 할일 작성하면 실행되는 함수)
def add_todo():
    print(f'함수가 호출 될 때 주머니에 담긴 값: {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    print(f'할 일 추가 후 객체의 상태: {todo}')  # 로그 확인
    # print(todo)
    st.session_state.todos.append(todo)
    st.session_state.new_task = ""

def toggle_done(index: int):
    todo = st.session_state.todos[index]
    todo.set_done(not todo.get_done())

# todos (todo 객체를 담을 리스트를 초기화)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# print(f'session_state에 new_task로 있는 값은?{st.session_state.new_task}')

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다.
st.text_input('새로운 할일 추가',key='new_task', on_change=add_todo)   # input 창에 내용을 작성(기존과 다른 내용)하고
                                                                          # 엔터하면 add_todo함수 호출

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i}번째 todo => {todo}')
        col1, col2 = st.columns([0.2, 0.9])  # 칸 비율은 []로 감싸줘야 %로 반환
        col1.checkbox(f'{i + 1}', value=todo.get_done(), key=f'done_{i}', on_change=toggle_done, args=(i,))
        col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())
else:
    st.info('할 일을 추가해 보세요.')