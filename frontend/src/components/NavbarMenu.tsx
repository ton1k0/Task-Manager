import {Avatar, Flex} from "@chakra-ui/react";
import {HomeIcon} from "../Icons/HomeIcon.tsx";
import {BellIcon} from "../Icons/BellIcon.tsx";
import {ChatIcon} from "../Icons/ChatIcon.tsx";
import {ProjectsIcon} from "../Icons/ProjectsIcon.tsx";

export function NavbarMenu() {
    return(
        <Flex
            zIndex={"1000000000"}
            flexDirection='column'
              gap='4'
              alignItems='center'
        >

            <Avatar _hover={{cursor: "pointer"}}
                    size='md'
                    borderRadius='20%'
                    name='Dan Abrahmov'
                    src='https://bit.ly/dan-abramov'
            />

            <HomeIcon/>

            <BellIcon/>
            <ChatIcon/>
            <ProjectsIcon />

        </Flex>
    )
}