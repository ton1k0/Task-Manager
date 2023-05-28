import { BrowserRouter as Router, Routes, Route, } from "react-router-dom";

import MainPage from "./pages/MainPage";

import {ChakraProvider} from "@chakra-ui/react";


function App() {

    return (

        <ChakraProvider>

            <Router>

                <Routes>

                    <Route path="/" element={<MainPage />}>

                    </Route>

                </Routes>

            </Router>

        </ChakraProvider>

    );
}


export default App;