import { BrowserRouter as Router, Routes, Route,} from "react-router-dom";
import {ChakraProvider} from "@chakra-ui/react";

import Sidebar from "./components/Sidebar.tsx";
import {Home} from "./components/Home.tsx";
import {Notify} from "./components/Notify.tsx";
import {Chat} from "./components/Chat.tsx";
import {Task} from "./components/Task.tsx";
import {Options} from "./components/Options.tsx";

function App() {
  return (
  <ChakraProvider>
    <Router>
        <Routes>
          <Route path="/" element={<Sidebar/>}/>
            <Route index element={<Home/>}/>
            <Route path="/notify" element={<Notify/>}/>
            <Route path="/chat" element={<Chat/>}/>
            <Route path="/task" element={<Task/>}/>
            <Route path="/options" element={<Options/>}/>
        </Routes>
    </Router>
  </ChakraProvider>
  );
}

export default App;