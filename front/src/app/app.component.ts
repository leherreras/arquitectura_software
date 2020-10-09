import { Component } from '@angular/core';
import {PokemonService} from './services/pokemon.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'software-arquitecture';

  constructor(
    private pokemonService: PokemonService
  ) {}

}
