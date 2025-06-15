import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { KnnPredictPayload, KnnPredictService } from '../../services/knn-predict.service';

@Component({
  selector: 'app-knn-predict',
  imports: [FormsModule],
  templateUrl: './knn-predict.component.html',
  styleUrl: './knn-predict.component.scss'
})
export class KnnPredictComponent {
  features: string = '';
  method: 'soft' | 'hard' = 'soft';
  kValue: number = 3;
  predictedClass: string | null = null;

  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(private _predictService: KnnPredictService) { }

  runPredict(): void {
    const payload: KnnPredictPayload = {
      features: this.features.split(';').map(f => Number(f.trim())),
      method: this.method,
      k: this.kValue
    }

    this.errorMessage = '';
    this.predictedClass = null;
    this.isLoading = true;

    this._predictService.predict(payload).subscribe({
      next: (response) => {
        this.isLoading = false;

        if (response &&
          response.hasOwnProperty('predicted_class') &&
          response.predicted_class != null) {
          this.predictedClass = response.predicted_class;
        } else {
          this.errorMessage = response?.error || 'Nieprawidłowa odpowiedź z serwera';
        }
      },
      error: (error) => {
        this.isLoading = false;

        if (error.error && error.error.detail) {
          this.errorMessage = Array.isArray(error.error.detail)
            ? error.error.detail.map((e: any) => e.msg).join(', ')
            : error.error.detail;
        } else if (error.error && typeof error.error === 'string') {
          this.errorMessage = error.error;
        } else if (error.message) {
          this.errorMessage = error.message;
        } else {
          this.errorMessage = `Błąd serwera: ${error.status || 'Nieznany błąd'}`;
        }
      }
    });
  }
}
