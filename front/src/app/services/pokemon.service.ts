import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PokemonService {

  constructor(private http: HttpClient) {
  }

  getAllAbilities(): Observable<any> {
    const path = environment.apiUrl + 'ability';
    return this.http.get(path);
  }

  getAllAbility(id: string): Observable<any> {
    const path = environment.apiUrl + 'ability/' + id;
    return this.http.get(path);
  }

  getAllCharacteristics(): Observable<any> {
    const path = environment.apiUrl + 'characteristic';
    return this.http.get(path);
  }

  getAllCharacteristic(id: string): Observable<any> {
    const path = environment.apiUrl + 'characteristic/' + id;
    return this.http.get(path);
  }

  getAllEggGroups(): Observable<any> {
    const path = environment.apiUrl + 'egg-group';
    return this.http.get(path);
  }

  getAllEggGroup(id: string): Observable<any> {
    const path = environment.apiUrl + 'egg-group/' + id;
    return this.http.get(path);
  }

  getAllGenders(): Observable<any> {
    const path = environment.apiUrl + 'gender';
    return this.http.get(path);
  }

  getAllGender(id: string): Observable<any> {
    const path = environment.apiUrl + 'gender/' + id;
    return this.http.get(path);
  }

  getAllGrowthRates(): Observable<any> {
    const path = environment.apiUrl + 'growth-rate';
    return this.http.get(path);
  }

  getAllGrowthRate(id: string): Observable<any> {
    const path = environment.apiUrl + 'growth-rate/' + id;
    return this.http.get(path);
  }

  getAllNatures(): Observable<any> {
    const path = environment.apiUrl + 'nature';
    return this.http.get(path);
  }

  getAllNature(id: string): Observable<any> {
    const path = environment.apiUrl + 'nature/' + id;
    return this.http.get(path);
  }

  getAllPokeathlonStates(): Observable<any> {
    const path = environment.apiUrl + 'pokeathlon-stat';
    return this.http.get(path);
  }

  getAllPokeathlonStat(id: string): Observable<any> {
    const path = environment.apiUrl + 'pokeathlon-stat/' + id;
    return this.http.get(path);
  }

  getAllPokemones(): Observable<any> {
    const path = environment.apiUrl + 'pokemon';
    return this.http.get(path);
  }

  getAllPokemon(id: string): Observable<any> {
    const path = environment.apiUrl + 'pokemon/' + id;
    return this.http.get(path);
  }
}
