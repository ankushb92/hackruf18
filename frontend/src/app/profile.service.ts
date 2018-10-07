import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { consts } from "src/app/consts";

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private http: HttpClient) {}

  updateUserProfile(first, last, age, currency, timezone) {
    return this.http.put(consts.UPDATE_USER_URL, {'
  }
}
