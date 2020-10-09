import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {PokemonService} from "../../services/pokemon.service";

@Component({
  selector: 'app-pokeathlon-stat',
  templateUrl: './pokeathlon-stat.component.html',
  styleUrls: ['./pokeathlon-stat.component.css']
})
export class PokeathlonStatComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): any {
    this.http.getAllPokeathlonStates().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }
}
