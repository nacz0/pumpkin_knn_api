import { TestBed } from '@angular/core/testing';

import { KnnPredictService } from './knn-predict.service';

describe('KnnPredictService', () => {
  let service: KnnPredictService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KnnPredictService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
