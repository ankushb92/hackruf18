import { Injectable } from '@angular/core';
import {consts} from "./consts";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class LogoutService {

  constructor(private http: HttpClient) { }

  logout(session) {
    return this.http.post(consts.LOGOUT_URL, {}, {headers: new HttpHeaders({'session': session})});
  }
}
