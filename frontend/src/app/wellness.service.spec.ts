import { TestBed } from '@angular/core/testing';

import { WellnessService } from './wellness.service';

describe('WellnessService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WellnessService = TestBed.get(WellnessService);
    expect(service).toBeTruthy();
  });
});
