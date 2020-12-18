import { Pane, Button } from 'evergreen-ui';
import Container from './Container';

const Layout = ({ children }) => {
  return (
    <>
      <Pane is="header" paddingY={10} borderBottom>
        <Container>
          <Pane
            display="flex"
            justifyContent="space-between"
            alignItems="center"
          >
            <Button appearance="minimal">Home</Button>
          </Pane>
        </Container>
      </Pane>
      <Pane paddingY={20}>
        <Container>{children}</Container>
      </Pane>
    </>
  );
};

export default Layout;
