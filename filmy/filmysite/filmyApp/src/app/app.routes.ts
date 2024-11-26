import { Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { HomePage } from './home/home.page';

export const routes: Routes = [
  {
    path: '',
    component: HomePage,
    providers: [HttpClientModule], // Adiciona o HttpClientModule para essa rota
  },
];