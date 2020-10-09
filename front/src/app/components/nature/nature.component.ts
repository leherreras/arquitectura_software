import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {PokemonService} from "../../services/pokemon.service";

@Component({
  selector: 'app-nature',
  templateUrl: './nature.component.html',
  styleUrls: ['./nature.component.css']
})
export class NatureComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): any {
    this.http.getAllNatures().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }
}
