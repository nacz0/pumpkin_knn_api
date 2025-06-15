import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export interface KnnPredictPayload {
  features: number[];
  method: 'soft' | 'hard';
  k: number;
}

export interface KnnPredictResponse {
  predicted_class?: string;
  error?: string;
}

@Injectable({
  providedIn: 'root'
})
export class KnnPredictService {

  private readonly BASE_URL = 'http://localhost:8000';

  constructor(private _http: HttpClient) { }

  predict(payload: KnnPredictPayload) {
    return this._http.post<KnnPredictResponse>(`${this.BASE_URL}/predict`, payload);
  }
}
