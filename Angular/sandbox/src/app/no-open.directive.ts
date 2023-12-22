import { Directive, HostListener } from '@angular/core';

@Directive({
  selector: '[no-open]',
  standalone: true
})
export class NoOpenDirective {

  @HostListener('click', ['$event'])
  onClick(event: MouseEvent): void {
    console.log('Clic sur le lien avec no-open détecté'); // Pour le débogage
    event.preventDefault();
  }
}
