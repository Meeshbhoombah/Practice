//
//  ViewController.swift
//  TipCalculator
//
//  Created by Rohan Mishra on 10/15/17.
//  Copyright © 2017 Augment. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    enum service {
        case poor
        case average
        case great
        case beautiful
    }

    @IBAction func resetCalculator(_ sender: Any) {
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override var prefersStatusBarHidden: Bool {
        return true
    }
}
