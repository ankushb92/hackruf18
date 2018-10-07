import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { consts } from "src/app/consts";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  login(username, password) {
    return this.http.post(consts.LOGIN_URL, {'username': username, "password": password});
  }


}
