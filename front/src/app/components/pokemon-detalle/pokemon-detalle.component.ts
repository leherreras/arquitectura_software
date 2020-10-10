import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {PokemonService} from '../../services/pokemon.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-pokemon-detalle',
  templateUrl: './pokemon-detalle.component.html',
  styleUrls: ['./pokemon-detalle.component.css']
})
export class PokemonDetalleComponent implements OnInit {
  dataResults: Pokemon;

  constructor(private http: PokemonService,private route: ActivatedRoute) {
  }

  
  ngOnInit(){
    var name = this.route.snapshot.paramMap.get('name');
    console.log(name);
    this.http.getAllPokemon(name).subscribe(
      (data: Pokemon) => {
        console.log(data.name);
        this.dataResults =  data;            
      }
    );
  }
  

}
export interface Pokemon {
  name: string; 
  base_experience: string;
  sprites: Sprites;

}

export interface Sprites {
  front_default: string; 
}

