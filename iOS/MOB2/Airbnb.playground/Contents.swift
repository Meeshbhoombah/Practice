/*
 * Make a request to the Airbnb API and model four properties that
 * make up an Airbnb listing.
 *
 * @meeshbhoombah
 *
 */

import Foundation
import PlaygroundSupport

var url = URL(string: "https://api.airbnb.com/v2/search_results")!
var token = "915pw2pnf4h1aiguhph5gc5b2"

var request = URLRequest(url: url)
request.httpMethod = "GET"
request.addValue(token, forHTTPHeaderField: "api-key")

let session = URLSession.shared

let downloadTask = session.dataTask(with: request) { (data, response, error) in
    if let data = data {
        let json = try? JSONSerialization.jsonObject(with: data, options: .allowFragments)
        print(json!)
    }
}

downloadTask.resume()
