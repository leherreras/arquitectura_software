import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {PokemonService} from "../../services/pokemon.service";

@Component({
  selector: 'app-egg-group',
  templateUrl: './egg-group.component.html',
  styleUrls: ['./egg-group.component.css']
})
export class EggGroupComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): void {
    this.http.getAllEggGroups().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }

}
