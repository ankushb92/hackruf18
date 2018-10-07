import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import { consts } from "src/app/consts";

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private http: HttpClient) {}


  updateUserProfile(user, session) {
    return this.http.put(consts.UPDATE_PROFILE_URL, user, { headers: new HttpHeaders({'session': session}) });
  }
}
