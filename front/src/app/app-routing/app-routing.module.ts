import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {PokemonComponent} from '../components/pokemon/pokemon.component';
import {AbilityComponent} from '../components/ability/ability.component';
import {CharacteristicComponent} from "../components/characteristic/characteristic.component";
import {EggGroupComponent} from "../components/egg-group/egg-group.component";
import {GenderComponent} from "../components/gender/gender.component";
import {GrowthRateComponent} from "../components/growth-rate/growth-rate.component";
import {NatureComponent} from "../components/nature/nature.component";
import {PokeathlonStatComponent} from "../components/pokeathlon-stat/pokeathlon-stat.component";
import {PokemonDetalleComponent} from "../components/pokemon-detalle/pokemon-detalle.component";
const routes: Routes = [
  {path: 'ability', component: AbilityComponent},
  {path: 'characteristic', component: CharacteristicComponent},
  {path: 'egg-group', component: EggGroupComponent},
  {path: 'gender', component: GenderComponent},
  {path: 'growth-rate', component: GrowthRateComponent},
  {path: 'nature', component: NatureComponent},
  {path: 'pokeathlon-stat', component: PokeathlonStatComponent},
  {path: 'pokemon', component: PokemonComponent},
  {path: 'pokemon-detalle/:name', component: PokemonDetalleComponent},
  {path: '**', component: PokemonComponent}
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {
}
