import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CharacteristicComponent } from './characteristic.component';

describe('CharacteristicComponent', () => {
  let component: CharacteristicComponent;
  let fixture: ComponentFixture<CharacteristicComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CharacteristicComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CharacteristicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
