import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {PokemonService} from "../../services/pokemon.service";

@Component({
  selector: 'app-gender',
  templateUrl: './gender.component.html',
  styleUrls: ['./gender.component.css']
})
export class GenderComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): any {
    this.http.getAllGenders().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }

}
