from django.shortcuts import redirect, render
from todo.models import TodoList

# Create your views here.
def create_todo(request):
	myTodo = TodoList()
	if request.method == 'POST':
		myTodo.todo = request.POST['todo']
		myTodo.description = request.POST['description']
		myTodo.important = request.POST.get('important') == "on"
		myTodo.complete = request.POST.get('complete') == "on"
		myTodo.save()
		return redirect('todos')
	return render(
		request,
		'todo/todo_create.html'
	)
def todos(request):
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/todos.html',
  		{
			'todolist': todolist,
			}
	)
def index(request):
	#todolist의 모든 레코드를 가져온다.
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/index.html',
		{
			#HTML에서 todolist라는 이름으로 todolist를 넘겨준다.
			'todolist': todolist,
		}
	)