import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {PokemonService} from "../../services/pokemon.service";

@Component({
  selector: 'app-growth-rate',
  templateUrl: './growth-rate.component.html',
  styleUrls: ['./growth-rate.component.css']
})
export class GrowthRateComponent implements OnInit {
  dataResults: Observable<any>;

  constructor(private http: PokemonService) {
  }

  ngOnInit(): void {
    this.http.getAllGrowthRates().subscribe(
      data => {
        console.log(data);
        this.dataResults = data;
      }
    );
  }
}
