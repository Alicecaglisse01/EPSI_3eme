export class Todo {
  constructor(
    public id: number,
    public title: string,
    public content: string,
    public author: string,
    public isCompleted: boolean,
    public createAt: Date,
    public completeAt: Date,
  ) {
    this.createAt = new Date();
  }
}
