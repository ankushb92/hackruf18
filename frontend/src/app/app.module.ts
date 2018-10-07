import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule, MatInputModule, MatButtonModule, MatMenuModule, MatIconModule, MatSnackBarModule, MatTabsModule, MatCardModule, MatDatepickerModule, MatNativeDateModule, MatDividerModule, MatChipsModule, MatExpansionModule} from '@angular/material';
import { FormsModule } from "@angular/forms";
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HttpClientModule }    from '@angular/common/http';
import { RootComponent } from './root/root.component';
import { ProfileComponent } from './profile/profile.component';
import { WellnessComponent } from './wellness/wellness.component';
import { AnalyticsComponent } from './analytics/analytics.component';
import { HistoryComponent } from './history/history.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RootComponent,
    ProfileComponent,
    WellnessComponent,
    AnalyticsComponent,
    HistoryComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    FormsModule,
    MatInputModule,
    MatButtonModule,
    HttpClientModule,
    MatMenuModule,
    MatIconModule,
    MatSnackBarModule,
    MatTabsModule,
    MatCardModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatDividerModule,
    MatChipsModule,
    MatExpansionModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
