import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PokemonDetalleComponent } from './pokemon-detalle.component';

describe('PokemonDetalleComponent', () => {
  let component: PokemonDetalleComponent;
  let fixture: ComponentFixture<PokemonDetalleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PokemonDetalleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PokemonDetalleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
