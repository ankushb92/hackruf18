import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { consts } from "src/app/consts";

@Injectable({
  providedIn: 'root'
})
export class HistoryService {

constructor(private http: HttpClient) { }

    get_history(session){
        return this.http.get(consts.HISTORY_URL, {headers: new HttpHeaders({'session': session})}); 
    }

    get_holdings(session){
        return this.http.get(consts.HOLDING_URL, {headers: new HttpHeaders({'session': session})}); 
    }
}
