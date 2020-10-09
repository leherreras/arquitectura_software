import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import {HttpClientModule} from '@angular/common/http';
import { CharacteristicComponent } from './components/characteristic/characteristic.component';
import { GenderComponent } from './components/gender/gender.component';
import { GrowthRateComponent } from './components/growth-rate/growth-rate.component';
import { NatureComponent } from './components/nature/nature.component';
import { PokeathlonStatComponent } from './components/pokeathlon-stat/pokeathlon-stat.component';
import { PokemonComponent } from './components/pokemon/pokemon.component';
import { EggGroupComponent } from './components/egg-group/egg-group.component';
import {AbilityComponent} from './components/ability/ability.component';
import {RouterModule} from '@angular/router';
import {AppRoutingModule} from './app-routing/app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HeaderComponent,
    AbilityComponent,
    CharacteristicComponent,
    GenderComponent,
    GrowthRateComponent,
    NatureComponent,
    PokeathlonStatComponent,
    PokemonComponent,
    EggGroupComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
