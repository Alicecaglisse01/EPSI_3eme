import { Component, Input } from '@angular/core';
import { Todo } from '../todo';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'todo',
  standalone: true,
  imports: [CommonModule],
  template: `
      <article *ngIf="todo" border-highlight>
        <div class="grid">
          <label for="todo-{{todo.id}}">
            <input
              type="checkbox"
              id="todo-{{todo.id}}"
              name="terms"
              [checked]="todo.isCompleted">
              {{ todo.title  }}
          </label>
          <div class="action">
            <a href="#">Edit</a>
            <a href="#">Delete</a>
          </div>
        </div>
      </article>

  `,
  styles: [
    `  
    .action {
      display: flex;
      flex-direction: row;
      justify-content: flex-end;
    }
    `
  ]
})
export class TodoComponent {
  @Input('value')
  todo: Todo | undefined;

  onCheck() {
    if (this.todo) {
      this.todo.isCompleted = !this.todo?.isCompleted;
      console.table(this.todo);
    }
  }
}
