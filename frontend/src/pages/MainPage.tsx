import {Flex,} from "@chakra-ui/react";
import {GearIcon} from "../Icons/GearIcon.tsx";
import {ExitIcon} from "../Icons/ExitIcon.tsx";
import {NavbarMenu} from "../components/NavbarMenu.tsx";




function MainPage() {
    return (
        <Flex>

            <Flex
                borderRadius='20'
                  bg='gray.100'
                  p={2}
                  minHeight='calc(100vh - 32px)'
                  justifyContent='space-between'
                  minWidth='max-content'
                  maxWidth='40px'
                  flexDirection='column'
                  alignItems='center'
                  marginLeft='2'
                  marginY='4'
            >

                <NavbarMenu/>

                <Flex
                    flexDirection='column'
                      gap='4'
                >
                    <GearIcon/>

                    <ExitIcon/>

                </Flex>
            </Flex>

        </Flex>
    );
}

export default MainPage;
