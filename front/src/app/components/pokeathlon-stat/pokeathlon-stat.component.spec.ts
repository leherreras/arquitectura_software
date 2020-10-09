import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PokeathlonStatComponent } from './pokeathlon-stat.component';

describe('PokeathlonStatComponent', () => {
  let component: PokeathlonStatComponent;
  let fixture: ComponentFixture<PokeathlonStatComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PokeathlonStatComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PokeathlonStatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
