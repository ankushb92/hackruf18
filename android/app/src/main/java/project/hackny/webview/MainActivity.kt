package project.hackny.webview

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebViewClient
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        view.settings.domStorageEnabled = true
        view.settings.javaScriptEnabled = true
        view.settings.javaScriptCanOpenWindowsAutomatically = true
        view.settings.databaseEnabled = true
        view.settings.setAppCacheEnabled(true)
        view.loadUrl("http://172.31.97.165:4200")
    }
}
