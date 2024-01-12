import { Injectable } from '@angular/core';
import { Todo } from './todo';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, map, of, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  todosUrl: string = 'api/todos';

  constructor(
    private http: HttpClient
  ) {}

  getTodoList(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.todosUrl).pipe(
      tap(todoList => console.log(todoList)),
      catchError(error => {
        console.log(error);
        return of([]);
      })
    );
  }

  getTodoById(id: number): Observable<Todo | undefined> {
    return this.http.get<Todo[]>(this.todosUrl).pipe(
      map(todoList => todoList.find(todo => todo.id === id))
    );
  }

}