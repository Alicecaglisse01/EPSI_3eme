import { Component } from '@angular/core';
import { CommonModule, getLocaleEraNames } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HighlightDirective } from './highlight.directive';
import { NoOpenDirective } from './no-open.directive';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HighlightDirective, NoOpenDirective],
  template: `
  <h1> Découverte des directives d'attributs </h1>
    <p highlight bg-color="blue" default-color="purple">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis quod aut itaque facilis neque cupiditate sunt sapiente, 
    quae nostrum iure! Enim dignissimos repellat temporibus, repellendus atque maxime quos labore. Dignissimos!</p>

    <p >Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis quod aut itaque facilis neque cupiditate sunt sapiente, 
    quae nostrum iure! Enim dignissimos repellat temporibus, repellendus atque maxime quos labore. Dignissimos!</p>

    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis quod aut itaque facilis neque cupiditate sunt sapiente, 
    quae nostrum iure! Enim dignissimos repellat temporibus, repellendus atque maxime quos labore. Dignissimos!</p>

    <a href="https://example.com" no-open>Ce lien ne s'ouvrira pas.</a>
  `,
  styleUrls: [ './app.component.css' ]
})
export class AppComponent {
  title = 'sandbox';
}