import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TODOS } from '../mock-todo';
import { BorderHighlightDirective } from '../border-highlight.directive';
import { TodoComponent } from '../todo/todo.component';
import { TodoService } from '../todo.service';
import { Todo } from '../todo';

@Component({
  selector: 'todo-list',
  standalone: true,
  imports: [CommonModule, BorderHighlightDirective, TodoComponent],
  template: `
    <h1>Liste des choses à faire</h1>

    <a href="#" role="button" [class.secondary]="!completedFilter && !completedAll" (click)="onClickTodo()">A faire</a>
    <a href="#" role="button" [class.secondary]="completedFilter && !completedAll" (click)="onClickTodoCompleted()">Terminées</a>
    <a href="#" role="button" [class.secondary]="completedAll" (click)="onClickAll()">Afficher Tout</a>
      <ng-container *ngFor="let todo of todoList">
        <todo *ngIf="todo.isCompleted === completedFilter" [value]=todo/>
      </ng-container>
    `,
  styles: []
})
export class TodoListComponent {
  todoList: Todo[] = [];

  completedFilter: boolean = false;
  completedAll: boolean = false;

  constructor(private todoService: TodoService) { }

  ngOnInit(): void {
    this.todoService.getTodoList().subscribe(todos => this.todoList = todos);
  }


  onClickTodo(): void {
    console.log("A faire");
    this.completedAll = false;
    this.completedFilter = false;
  }

  onClickTodoCompleted(): void {
    console.log("Terminée");
    this.completedAll = false;
    this.completedFilter = true;
  }

  onClickAll(): void {
    this.completedAll = true
}
}