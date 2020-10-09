import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EggGroupComponent } from './egg-group.component';

describe('EggGroupComponent', () => {
  let component: EggGroupComponent;
  let fixture: ComponentFixture<EggGroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EggGroupComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EggGroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
