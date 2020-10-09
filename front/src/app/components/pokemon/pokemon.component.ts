import {Component, OnInit} from '@angular/core';
import {PokemonService} from '../../services/pokemon.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-pokemon',
  templateUrl: './pokemon.component.html',
  styleUrls: ['./pokemon.component.css']
})
export class PokemonComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): any {
    this.http.getAllPokemones().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }
}
