import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { KnnPredictComponent } from "./components/knn-predict/knn-predict.component";

@Component({
  selector: 'app-root',
  imports: [KnnPredictComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent { }
